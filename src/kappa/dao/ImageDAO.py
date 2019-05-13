from kappa.dao.DAO import DAO
from kappa.dao import ConnectionManager
from kappa.models.ImageModel import ImageModel
from kappa.controllers.FaceVectorController import FaceVectorController
from kappa.controllers.ObjectVectorController import ObjectVectorController
from kappa.dao.ObjectVectorDAO import ObjectVectorDAO
from kappa.dao.FaceVectorDAO import FaceVectorDAO

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
