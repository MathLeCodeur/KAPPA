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


	def importObjectVectors(self):
		#recuperation du fichier des description de chaque vecteurs
		descriptionf = open('C:\\Users\\Alexis\\Desktop\\Nouveaudossier\\KAPPA\\res\\database\\imagenet_synset_to_human_label_map.txt','r')
		descriptionlines  = descriptionf.readlines()
		descriptionf.close()

		#recuperation du fichier des lien parent pour chaque vecteurs
		parentf= open('C:\\Users\\Alexis\\Desktop\\Nouveaudossier\\KAPPA\\res\\database\\wordnet.is_a.txt','r')
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
			if (vectorEnfant in tags):
				tags[vectorEnfant] = ( tags[vectorEnfant] , vectorParent )


		#pour les grand parent on leur met des parents null
		for vector, tags_and_parent in tags.items():
			if(type(tags_and_parent)!= type((88,55))):
				tags[vector] = ( tags[vector] , None )
		
		#printOne(tags)

		#/////////////////////////////////////////////////////////////////////////
		#////////////////////////////SQL REQUEST HERE/////////////////////////////
		#/////////////////////////////////////////////////////////////////////////

		for vector, tags_and_parent in tags.items():

			#exemple :
			#vector          => 'n07877187'
			#tags_and_parent => ('spaghetti and meatballs', 'n07557434')
			if (isinstance(tags_and_parent[0], tuple)) :
				continue

			vChild = self.cDao.getByValue(vector)

			if (vChild!=None) :
				vChild.value = vector
				vChild.tagName = tags_and_parent[0]
				if(tags_and_parent[1]==None) :
					vChild.parent = None
				else :
					vParent = self.cDao.getByValue(tags_and_parent[1])
					if(vParent!=None) :
						vChild.parent = vParent.id
					else :
						nextId=self.cDao.getNextId()
						vParent = ObjectVectorModel(nextId, tags_and_parent[1], "", None)
						vChild.parent = nextId
						self.cDao.create(vParent)
				self.cDao.update(vChild)
			else :
				nextId=self.cDao.getNextId()
				vChild = ObjectVectorModel(nextId, vector, tags_and_parent[0], None)
				if(tags_and_parent[1]==None) :
					vChild.parent = None
				else :
					vParent = self.cDao.getByValue(tags_and_parent[1])
					if(vParent!=None) :
						vChild.parent = vParent.id
					else :
						vParent = ObjectVectorModel(nextId+1, tags_and_parent[1], "", None)
						vChild.parent = nextId+1
						print(vChild.parent)
						self.cDao.create(vParent)
				self.cDao.create(vChild)

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
