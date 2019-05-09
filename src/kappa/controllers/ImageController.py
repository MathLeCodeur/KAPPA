from kappa.dao.DAO import DAO
from kappa.controllers.Controller import Controller
from kappa.dao import ConnectionManager
from kappa.models.ImageModel import ImageModel
from kappa.dao.ImageDAO import ImageDAO


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
		y = ConnectionManager.ConnectionManager('KappaBase.db')
		l=os.listdir(pathF)

		#get next id
		ui=y.executeSQL("select Max(id_image) from Image")
		u=ui
		for elem in ui:
			if(elem[0] == None):
				u=0
				break
			u=elem[0]+1

		#file in folder
		for i in l:
			print(i)
			if(os.path.isfile(pathF+i)):

				extension = i.split(".")[1]
				if(extension in ("jpeg","jpg","png","PNG","JPEG","JPG")):

					im = Image.open(pathF+str(i))
					path = pathF+str(i)
					size = os.path.getsize(path)
					width = im.size[0]
					height = im.size[1]
					date = str(time.ctime(os.path.getctime(pathF+str(i))))
					sql	= "Insert into IMAGE (id_image,creation_date ,length, width,size, path) values ("+str(u)+",'"+date+"',"+str(height)+", "+str(width)+ ", " +str(size)+", '" +path+"')"
					print(path)
					#y.executeAndCommitSQL(sql)
					u+=1
