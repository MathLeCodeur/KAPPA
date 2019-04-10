import kappa.dao.DAO as dao
import kappa.controllers.Controller as ctl
from kappa.dao import ConnectionManager
import kappa.models.ImageModel as im
from kappa.dao.ImageDAO import ImageDAO
import os
import glob
from PIL import Image
import time


class ImageController(ctl.Controller):
	def __init__(self):
		super().__init__()
		self.cDao = ImageDAO()

	def getAll(self):
		return self.cDao.getAll()

	def getById(self):
		print("coucou")

	def importImageFolder(self,pathF):
		y = ConnectionManager.ConnectionManager('KappaBase.db')
		print(y.instance.connection)
		l=os.listdir(pathF)
		ui=y.executeSQL("select Max(id_image) from Image");
		u=ui
		for elem in ui:
			if(elem[0] == None):
				u=0
				break
			u=elem[0]+1
		#print(ui)
		for i in l:
			im = Image.open(pathF+str(i))
			path = pathF+str(i)
			size = os.path.getsize(path)
			width = im.size[0]
			height = im.size[1]
			date = str(time.ctime(os.path.getctime(pathF+str(i))))
			sql = "Insert into IMAGE (id_image,creation_date ,length, width,size, path) values ("+str(u)+",'"+date+"',"+str(height)+", "+str(width)+ ", " +str(size)+", '" +path+"')"
			print(sql)
			y.executeAndCommitSQL(sql)
			u+=1
