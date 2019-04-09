import DAO as dao
import Controller as ctl
import ConnectionManager
import ImageModel as im
from ImageDAO import ImageDAO



class ImageController(ctl.Controller):
	def __init__(self):
		super().__init__()
		self.cDao = ImageDAO()

	def getAll(self):
		return self.cDao.getAll()

	def getById(self):
		print("coucou")
