from kappa.dao.DAO import DAO
from kappa.controllers.Controller import Controller
from kappa.dao import ConnectionManager
from kappa.models.ImageModel import ImageModel
from kappa.dao.ImageDAO import ImageDAO
import os
import glob
from PIL import Image
import time
#from NodeLookup import NodeLookup,searchTags,run_inference_on_image,create_graph
import kappa.controllers.NodeLookup

class ImageController(Controller):
	def __init__(self):
		super().__init__()
		self.cDao = ImageDAO()

	def getAll(self):
		return self.cDao.getAll()

	def getAllOrderByDate(self):
		return self.cDao.getAllOrderByDate()

	def getById(self,id):
		return self.cDao.getById(id)

	def linkToVector(self,imgModel, vector):
		self.cDao.linkToVector(imgModel,vector)

	def importImageFolder(self,pathF):

		l=os.listdir(pathF)

		#get next id
		u=self.cDao.getNextId()

		listImage = self.cDao.getAll()
		listPath =[]
		for im in listImage:
			listPath.append(im.path)

		#file in folder
		for i in l:
			pathName = pathF+i
			if(os.path.isfile(pathName) and pathName not in listPath):

				extension = i.split(".")[1]
				if(extension in ("jpeg","jpg","png","PNG","JPEG","JPG")):
					im = Image.open(pathF+str(i))
					path = pathF+str(i)
					size = os.path.getsize(path)
					width = im.size[0]
					height = im.size[1]
					date = str(time.ctime(os.path.getctime(pathF+str(i))))
					sql	= "Insert into IMAGE (id_image,creation_date ,length, width,size, path) values ("+str(u)+",'"+date+"',"+str(height)+", "+str(width)+ ", " +str(size)+", '" +path+"')"
					print("image insert" + path)
					y.executeAndCommitSQL(sql)
					u+=1

	def searchTags(self, pathIm):
		return kappa.controllers.NodeLookup.searchTags(pathIm)
		
		
		
	def getAllTags(objV):
		listTagHere = []   # on rempli le tag de l'image actuel et ses parents
		while(objV != NULL ):
			listTagHere.append(objV.tagName)
			objV = objV.parents
		return listTagHere


	def getSimilarScoreTags(taglist1 , taglist2):
		score = 0 
		for tag1 in taglist1:
			for tag2 in taglist2:
				if(tag1 == tag2):
					score+=1
		return score


	def searchSimilar(self):
		listTagHere = getAllTags(self.objectVectors.tagName)  # on rempli le tag de l'image actuel et ses parents
		#on vas comparer aux tags des autres images
		imageList= self.cDao.getAll()
		scoreList=[]
		for img in imageList : 
			s = getSimilarScoreTags(listTagHere , getAllTags(img.objectVectors))
			score.append([s,img])# on initialise un score de similarité pour tout le monde
			
		scoreList.sort(key=lambda x: x[0])
		
		finalList = []
		for img in scoreList:
			if(img[0] > 1):
				finalList.append(img[1])
		return finalList
		
		
				

