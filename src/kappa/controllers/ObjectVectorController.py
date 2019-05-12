from kappa.controllers.Controller import Controller
from kappa.dao import ConnectionManager
from kappa.models.ObjectVectorModel import ObjectVectorModel
from kappa.dao.ObjectVectorDAO import ObjectVectorDAO
import os
import glob
from PIL import Image
import time


class ObjectVectorController(Controller):
	def __init__(self):
		super().__init__()
		self.cDao = ObjectVectorDAO()

	def update(self, vectorModel):
		self.cDao.update(vectorModel)

	def create(self, vectorModel):
		self.cDao.create(vectorModel)

	def getAll(self):
		return self.cDao.getAll()

	def getByImageId(self, id):
		return self.cDao.getByImageId(id)

	def getById(self, id):
		return self.cDao.getById(id)

	def getByValue(self, value):
		return self.cDao.getByValue(value)

	def getNextId(self):
		return self.cDao.getNextId()

	def delete(self, oVectModel):
		self.cDao.delete(oVectModel)

	def importObjectVectors(self):
		#recuperation du fichier des description de chaque vecteurs
		descriptionf = open('./res/database/imagenet_synset_to_human_label_map.txt','r')
		descriptionlines  = descriptionf.readlines()
		descriptionf.close()

		#recuperation du fichier des lien parent pour chaque vecteurs
		parentf= open('./res/database/wordnet.is_a.txt','r')
		parentslines  = parentf.readlines()
		parentf.close()



		#on transforme les description en tuple
		tags={}
		for description in descriptionlines:
			tags[description[:9]] = description[10:-1]
		#printOne(tags)



		#on ajoute les parents dans le tuples
		for parent in parentslines:
			# in file : parent - enfant
			vectorParent =parent[:9]
			vectorEnfant = parent[10:-1]
			if (vectorEnfant in tags and vectorParent in tags and not isinstance(tags[vectorEnfant], tuple) ):
				tags[vectorEnfant] = ( tags[vectorEnfant] , vectorParent )


		#pour les grand parent on leur met des parents null
		for vector, tags_and_parent in tags.items():
			if(type(tags_and_parent)!= type((88,55))):
				tags[vector] = ( tags[vector] , None )

		#printOne(tags)

		#/////////////////////////////////////////////////////////////////////////
		#////////////////////////////SQL REQUEST HERE/////////////////////////////
		#/////////////////////////////////////////////////////////////////////////

		self.cDao.importObjectVectors(tags.items())

		#/////////////////////////////////////////////////////////////////////////
		#/////////////////////////////////////////////////////////////////////////
		#/////////////////////////////////////////////////////////////////////////
