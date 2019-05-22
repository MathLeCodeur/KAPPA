from kappa.dao.DAO import DAO
from kappa.controllers.Controller import Controller
from kappa.dao.ConnectionManager import ConnectionManager
from kappa.models.ImageModel import ImageModel
from kappa.dao.ImageDAO import ImageDAO
from kappa.controllers.ObjectVectorController import ObjectVectorController
import kappa.object_detection.NodeLookup as NodeLookup
from os import listdir
from os.path import isdir, join, getctime, getsize, isfile
from PIL.Image import open
from datetime import datetime

class ImageController(Controller):
	def __init__(self):
		super().__init__()
		self.cDao = ImageDAO()

	def create(self, imgModel):
		ovc = ObjectVectorController()
		resTag = self.searchTags(imgModel.path, 0)

		for valueTag , score in resTag.items():
			if(imgModel.objectVectors==None) :
				imgModel.objectVectors = []
			imgModel.objectVectors.append(ovc.getByValue(valueTag))

		self.cDao.create(imgModel)

	def getAll(self):
		return self.cDao.getAll()

	def getAllOrderByDate(self):
		return self.cDao.getAllOrderByDate()

	def getByImageQuery(self, imageQuery):
		return self.cDao.getByImageQuery(imageQuery)

	def getById(self,id):
		return self.cDao.getById(id)

	def linkToVector(self,imgModel, vector):
		self.cDao.linkToVector(imgModel,vector)

	def importImageFolder(self,pathF):
		print(pathF)
		y = ConnectionManager('KappaBase.db')
		l=listdir(pathF)

		#get next id
		u=self.cDao.getNextId()

		listImage = self.cDao.getAll()
		listPath =[]
		for im in listImage:
			listPath.append(im.path)

		#file in folder
		for i in l:
			pathName = join(pathF, i)
			print(pathName)
			if(isfile(pathName) and pathName not in listPath):
				print(2, pathName)

				extension = i.split(".")[1]
				if(extension in ("jpeg","jpg","png","PNG","JPEG","JPG")):
					im = open(pathName)
					path = pathName
					size = getsize(path)
					width = im.size[0]
					height = im.size[1]
					date = str(datetime.fromtimestamp(getctime(path)))

					img = ImageModel(u, "", date, height, width, size, path, None, None)
					self.create(img)
					u+=1

	def searchTags(self, pathIm, score):
		return NodeLookup.searchTags(pathIm, score)



	def getAllTags(self, objVectors):
		listTagHere = []   # on rempli le tag de l'image actuel et ses parents
		maxi = 2
		for objV in objVectors:
			i=0
			while(objV != None and i < maxi  ):
				i=i+1
				listTagHere.append(objV.tagName)
				objV = objV.parent
		return listTagHere


	def getSimilarScoreTags(self, taglist1 , taglist2):
		score = 0
		for tag1 in taglist1:
			for tag2 in taglist2:
				if(tag1 == tag2):
					score+=1
		return score


	def searchSimilar(self, imgBase ):
		# on rempli le tag de l'image actuel et ses parents
		listTagHere = self.getAllTags(imgBase.objectVectors)
		#on vas comparer aux tags des autres images
		imageList= self.cDao.getAll()
		scoreList=[]
		for img in imageList :
			s = self.getSimilarScoreTags(listTagHere , self.getAllTags(img.objectVectors))
			scoreList.append([s,img])# on initialise un score de similarité pour tout le monde
		scoreList.sort(key=lambda x: -x[0])

		finalList = []
		for img in scoreList:
			#print("score =  ",img[0], " : ", img[1].path)
			if(img[0] > 1):
				if(imgBase.path != img[1].path ):
				    finalList.append(img[1])
		return finalList
