import DAO as dao
import ConnectionManager
import VectorModel as vm



class VectorDAO(dao.DAO):
	def __init__(self):
		super().__init__()

	def getAll(self):
		cm = ConnectionManager.ConnectionManager('KappaBase.db')
		res = cm.executeSQL("SELECT * FROM Vector")
		vectorList = []
		for elem in res:
			vectorList.append(vm.VectorModel(elem[0], elem[1], "tagname", "parent"))
		return vectorList

	def getById(self):
		print("coucou")
