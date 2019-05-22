from kappa.dao.DAO import DAO
from kappa.dao.VectorDAO import VectorDAO
from kappa.dao import ConnectionManager
from kappa.models.VectorModel import VectorModel
from kappa.models.FaceVectorModel import FaceVectorModel


class FaceVectorDAO(DAO):
	def __init__(self):
		super(FaceVectorDAO, self).__init__()

	def getAll(self):
		cm = ConnectionManager.ConnectionManager('KappaBase.db')
		res = cm.executeSQL("SELECT * FROM Vector NATURAL JOIN Face_vector")
		vectorList = []
		for elem in res:
			i=0
			vectorList.append(FaceVectorModel(elem[0], elem[1], elem[2], elem[3]))
		return vectorList

	def create(self, FaceVectorModel):
		print("create")
		cm = ConnectionManager.ConnectionManager('KappaBase.db')
		vDao = VectorDAO()
		vDao.create(VectorModel(FaceVectorModel.id, FaceVectorModel.value, FaceVectorModel.tagName))
		res = cm.executeAndCommitSQL("INSERT INTO Face_vector (id_vector, IsKnown) VALUES (" + str(FaceVectorModel.id) + ", " + str(FaceVectorModel.isKnown) + ")")

	def getById(self, id):
		cm = ConnectionManager.ConnectionManager('KappaBase')
		res = cm.executeSQL("SELECT * FROM Vector NATURAL JOIN Face_vector WHERE id_vector=" + str(id))
		if (len(res)!=1) :
			return

		res = FaceVectorModel(res[0][0], res[0][1], res[0][2], res[0][3])

		return res

	def getKnown(self):
		cm = ConnectionManager.ConnectionManager('KappaBase.db')
		res = cm.executeSQL("SELECT * FROM Vector NATURAL JOIN Face_vector WHERE IsKnown=true")
		vectorList = []
		for elem in res:
			i=0
			vectorList.append(FaceVectorModel(elem[0], elem[1], elem[2], elem[3]))
		return vectorList

	def getByImageId(self, id):
		cm = ConnectionManager.ConnectionManager('KappaBase.db')
		res = cm.executeSQL("select * from Vector NATURAL JOIN FACE_VECTOR NATURAL JOIN INCLUDE where id_image = "+str(id)+";")
		vectorList = []
		for elem in res:
			vectorList.append(FaceVectorModel(elem[0], elem[1], elem[2], elem[3]))
		return vectorList

	def getByValue(self, value):
		cm = ConnectionManager.ConnectionManager('KappaBase')
		res = cm.executeSQL("SELECT * FROM Vector NATURAL JOIN Face_vector WHERE value_Vector=\"" + str(value)+"\";")
		if (len(res)!=1) :
			return

		res = FaceVectorModel(res[0][0], res[0][1], res[0][2], res[0][3])

		return res

	def getNextId(self):
		cm = ConnectionManager.ConnectionManager('KappaBase')
		res = cm.executeSQL("SELECT MAX(id_vector) FROM VECTOR")
		res2 = res
		for elem in res:
			if(elem[0] == None):
				res2=0
				break
			res2=elem[0]+1
		return res2
	def delete(self,faceVectorModel):
		cm = ConnectionManager.ConnectionManager('KappaBase')
		vDao = VectorDAO()
		vDao.delete(VectorModel(faceVectorModel.id, faceVectorModel.value, faceVectorModel.tagName))
		cm.executeAndCommitSQL("Delete from face_vector WHERE id_vector=" + str(faceVectorModel.id))

	def update(self, faceVectorModel):
		cm = ConnectionManager.ConnectionManager('KappaBase')
		vDao = VectorDAO()
		vDao.update(VectorModel(faceVectorModel.id, faceVectorModel.value, faceVectorModel.tagName))
		cm.executeAndCommitSQL("UPDATE face_vector SET IsKnown=" + str(faceVectorModel.isKnown)+ " WHERE id_vector=" + str(faceVectorModel.id))
