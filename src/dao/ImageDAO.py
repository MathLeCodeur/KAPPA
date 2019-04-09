import DAO as dao
import ConnectionManager
import ImageModel as im



class ImageDAO(dao.DAO):
	def __init__(self):
		super().__init__()

	def getAll(self):
		cm = ConnectionManager.ConnectionManager('KappaBase.db')
		res = cm.executeSQL("SELECT * FROM Image")
		imageList = []
		for elem in res:
			print(elem)
			imageList.append(im.ImageModel(elem[0], elem[1],elem[2],elem[3],elem[4],elem[5],elem[6], "face", "obj"))
		return imageList

	def getById(self):
		print("coucou")



