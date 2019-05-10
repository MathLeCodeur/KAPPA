import kappa.dao.DAO as dao
import kappa.controllers.Controller as ctl
from kappa.dao import ConnectionManager
from kappa.models.ObjectVectorModel import ObjectVectorModel
from kappa.dao.ObjectVectorDAO import ObjectVectorDAO
import os
import glob
from PIL import Image
import time


class ObjectVectorController(ctl.Controller):
	def __init__(self):
		super().__init__()
		self.cDao = ObjectVectorDAO()

	def getByImageId(self, id):
		return self.cDao.getByImageId(id)

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

	def printOne(tags):
		i=0
		for vector, tag_et_parent in tags.items():
			i=i+1
			if(i==1):
				print('tags0=',vector," = ", tag_et_parent)
				#print('type=',type(tag_et_parent))
				break

	def getRecognizedObjects(self, imagePath: str):
		objects = []

		return objects
