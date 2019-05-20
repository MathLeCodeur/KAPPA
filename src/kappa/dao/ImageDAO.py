from kappa.dao.DAO import DAO
from kappa.dao import ConnectionManager
from kappa.models.ImageModel import ImageModel
from kappa.controllers.FaceVectorController import FaceVectorController
from kappa.controllers.ObjectVectorController import ObjectVectorController
from kappa.dao.ObjectVectorDAO import ObjectVectorDAO
from kappa.dao.FaceVectorDAO import FaceVectorDAO
from kappa.interoperability.image_query import *

class ImageDAO(DAO):
    def __init__(self):
        super().__init__()

    def getAllOrderByDate(self):
        cm = ConnectionManager.ConnectionManager('KappaBase.db')

        res = cm.executeSQL("SELECT * FROM Image order by creation_date")
        oVectDao = ObjectVectorDAO()
        fVectDao = FaceVectorDAO()
        imageList = []
        for elem in res:
            imageList.append(ImageModel(elem[0], elem[1],elem[2],elem[3],elem[4],elem[5],elem[6], fVectDao.getByImageId(elem[0]), oVectDao.getByImageId(elem[0])))
        return imageList

    def getAll(self):
        cm = ConnectionManager.ConnectionManager('KappaBase.db')
        res = cm.executeSQL("SELECT * FROM Image")
        oVectDao = ObjectVectorDAO()
        fVectDao = FaceVectorDAO()
        imageList = []
        for elem in res:
            imageList.append(ImageModel(elem[0], elem[1],elem[2],elem[3],elem[4],elem[5],elem[6], fVectDao.getByImageId(elem[0]), oVectDao.getByImageId(elem[0])))
        return imageList

    def getByImageQuery(self, imageQuery):
        cm = ConnectionManager.ConnectionManager('KappaBase.db')
        res = cm.executeSQL(self.convertImageQueryToSQL(imageQuery))
        oVectDao = ObjectVectorDAO()
        fVectDao = FaceVectorDAO()
        imageList = []
        for elem in res:
            imageList.append(ImageModel(elem[0], elem[1],elem[2],elem[3],elem[4],elem[5],elem[6], fVectDao.getByImageId(elem[0]), oVectDao.getByImageId(elem[0])))
        return imageList

    def getById(self,id):
        cm = ConnectionManager.ConnectionManager('KappaBase.db')
        res = cm.executeSQL("SELECT * FROM Image where id_image ="+id+";")
        return res

    def getNextId(self):
        cm = ConnectionManager.ConnectionManager('KappaBase')
        res = cm.executeSQL("SELECT MAX(id_image) FROM IMAGE")
        res2 = res
        for elem in res:
            if(elem[0] == None):
                res2=0
                break
            res2=elem[0]+1

        return res2

    def linkToVector(self,imgModel, vector):
        cm = ConnectionManager.ConnectionManager('KappaBase.db')
        res = cm.executeAndCommitSQL("INSERT INTO Include (id_image, id_vector) VALUES (" + str(imgModel.id) + ","+ str(vector.id)+ ")")

    def update(self, imageMod):
        print("update")

    def create(self, imgModel):
        cm = ConnectionManager.ConnectionManager('KappaBase.db')
        res = cm.executeAndCommitSQL("INSERT INTO Image (id_image, comment,creation_date,length,width,size,path)" +
                                    "VALUES (" + str(imgModel.id) + ", \"" + imgModel.comment + "\", \"" + imgModel.creation_date + "\", " + str(imgModel.length) + "," + str(imgModel.width) + "," + str(imgModel.size) + ",\"" + imgModel.path+"\")")
        if (imgModel.objectVectors==None):
            return
        for ov in imgModel.objectVectors:
            self.linkToVector(imgModel, ov)

    def convertImageQueryToSQL(self, imageQuery):
        sqlQuery = 'SELECT * FROM IMAGE NATURAL JOIN INCLUDE NATURAL JOIN VECTOR'
        conditions = imageQuery.getConditions()

        nameSqlConditions = []
        dateSqlConditions = []
        tagsSqlConditions = []

        if conditions:
            sqlQuery += ' WHERE '
            for i in range(len(conditions)):
                condition = conditions[i]
                sqlCondition = ''

                field = condition.getField()
                if field == ImageQueryField.NAME:
                    sqlCondition += 'path'
                    sqlConditionContainer = nameSqlConditions
                elif field == ImageQueryField.DATE:
                    sqlCondition += "strftime('%Y-%m-%d', creation_date)"
                    sqlConditionContainer = dateSqlConditions
                elif field == ImageQueryField.TAGS:
                    sqlCondition += 'tag_name'
                    sqlConditionContainer = tagsSqlConditions
                else:
                    raise ValueError()

                operator = condition.getOperator()
                if operator == ImageQueryOperator.EQUALS:
                    sqlCondition += ' = '
                elif operator == ImageQueryOperator.GREATER_THAN:
                    sqlCondition += ' > '
                elif operator == ImageQueryOperator.LOWER_THAN:
                    sqlCondition += ' < '
                elif operator == ImageQueryOperator.BETWEEN:
                    sqlCondition += ' BETWEEN '
                elif operator == ImageQueryOperator.CONTAINS:
                    sqlCondition += ' LIKE '
                else:
                    raise ValueError()

                operand1, operand2 = condition.getOperand1(), condition.getOperand2()
                if field == ImageQueryField.DATE:
                    operand1 = str(ImageQuery.parseDate(operand1))
                    if operand2: operand2 = str(ImageQuery.parseDate(operand2))
                operand1 = operand1.replace("'","''")
                if operand2: operand2 = operand2.replace("'","''")

                if operator == ImageQueryOperator.BETWEEN:
                    sqlCondition += "'" + operand1 + "' AND '" + operand2 + "'"
                elif operator == ImageQueryOperator.CONTAINS:
                    sqlCondition += "'%" + operand1 + "%'"
                else:
                    sqlCondition += "'" + operand1 + "'"

                sqlConditionContainer.append(sqlCondition)

            sqlQuery += '(' + ') AND ('.join(
                ([' OR '.join(nameSqlConditions)] if nameSqlConditions else []) +
                ([' OR '.join(dateSqlConditions)] if dateSqlConditions else []) +
                ([' OR '.join(tagsSqlConditions)] if tagsSqlConditions else [])
            ) + ')'

        orderField = imageQuery.getImageGrouping()
        if orderField == ImageGrouping.DATE:
            sqlQuery += ' GROUP BY id_image ORDER BY creation_date'
        elif orderField == ImageGrouping.TAG:
            sqlQuery += ' ORDER BY tag_name'
        else:
            raise ValueError()

        sqlQuery += ';'
        print(sqlQuery)
        return sqlQuery
