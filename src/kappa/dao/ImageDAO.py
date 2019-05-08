import kappa.dao.DAO as dao
from kappa.dao import ConnectionManager
import kappa.models.ImageModel as im
from kappa.controllers.FaceVectorController import FaceVectorController
from kappa.controllers.ObjectVectorController import ObjectVectorController


class ImageDAO(dao.DAO):
	def __init__(self):
		super().__init__()

	def getAllOrderByDate(self):
		cm = ConnectionManager.ConnectionManager('KappaBase.db')
		res = cm.executeSQL("SELECT * FROM Image order by creation_date")
		oVectCtl = ObjectVectorController()
		fVectCtl = FaceVectorController()
		imageList = []
		for elem in res:
			imageList.append(im.ImageModel(elem[0], elem[1],elem[2],elem[3],elem[4],elem[5],elem[6], fVectCtl.getByImageId(elem[0]), oVectCtl.getByImageId(elem[0])))
		return imageList

	def getAll(self):
		cm = ConnectionManager.ConnectionManager('KappaBase.db')
		res = cm.executeSQL("SELECT * FROM Image")
		oVectCtl = ObjectVectorController()
		fVectCtl = FaceVectorController()
		imageList = []
		for elem in res:
			imageList.append(im.ImageModel(elem[0], elem[1],elem[2],elem[3],elem[4],elem[5],elem[6], fVectCtl.getByImageId(elem[0]), oVectCtl.getByImageId(elem[0])))
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
		print("create")
		cm = ConnectionManager.ConnectionManager('KappaBase.db')
		res = cm.executeAndCommitSQL("INSERT INTO Image (id_image, comment,creation_date,length,width,size,path) VALUES (" + imgModel.id + ", \"" + imgModel.comment + "\""+imgModel.creation_date+", "+imgModel.length+","+imgModel.size+","+imgModel.path+")")
