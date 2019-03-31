import DAO as dao
import ConnectionManager as cm
import VectorModel as vm



class VectorDAO(dao.DAO):
	def __init__(self):
		super().__init__(self)

	def getAll(self):
		res = self.connectionManager.executeSQL("SELECT * FROM Vector")
		vectorList = []
		for elem in res:
			vectorList.append(vm.VectorModel(elem[0], elem[1]))
		return vectorList

	def getById(self):
		print("coucou")
