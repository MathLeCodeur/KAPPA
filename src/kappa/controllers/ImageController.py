from kappa.dao.DAO import DAO
from kappa.controllers.Controller import Controller
from kappa.dao.ConnectionManager import ConnectionManager
from kappa.models.ImageModel import ImageModel
from kappa.dao.ImageDAO import ImageDAO
from kappa.controllers.ObjectVectorController import ObjectVectorController
import kappa.object_detection.NodeLookup as NodeLookup
import os
import glob
from PIL import Image
import time

class ImageController(Controller):
	def __init__(self):
		super().__init__()
		self.cDao = ImageDAO()

	def create(self, imgModel):
		ovc = ObjectVectorController()
		resTag = self.searchTags(imgModel.path, 0)

		for name , score in resTag.items():
			if(imgModel.objectVectors==None) :
				imgModel.objectVectors = []
			imgModel.objectVectors.append(ovc.getByName(name))

		self.cDao.create(imgModel)

	def getAll(self):
		return self.cDao.getAll()

	def getAllOrderByDate(self):
		return self.cDao.getAllOrderByDate()

	def getById(self,id):
		return self.cDao.getById(id)

	def linkToVector(self,imgModel, vector):
		self.cDao.linkToVector(imgModel,vector)

	def importImageFolder(self,pathF):
		print(pathF)
		y = ConnectionManager('KappaBase.db')
		l=os.listdir(pathF)

		#get next id
		u=self.cDao.getNextId()

		listImage = self.cDao.getAll()
		listPath =[]
		for im in listImage:
			listPath.append(im.path)

		#file in folder
		for i in l:
			pathName = os.path.join(pathF, i)
			print(pathName)
			if(os.path.isfile(pathName) and pathName not in listPath):
				print(2, pathName)

				extension = i.split(".")[1]
				if(extension in ("jpeg","jpg","png","PNG","JPEG","JPG")):
					im = Image.open(pathName)
					path = pathName
					size = os.path.getsize(path)
					width = im.size[0]
					height = im.size[1]
					date = str(time.ctime(os.path.getctime(path)))

					img = ImageModel(u, "", date, height, width, size, path, None, None)
					self.create(img)
					u+=1

	def searchTags(self, pathIm, score):
		return NodeLookup.searchTags(pathIm, score)
