from DAO import DAO as daoclass
from ConnectionManager import ConnectionManager
from VectorModel import VectorModel



class VectorDAO(daoclass):
	def __init__(self):
		super(VectorDAO, self).__init__()

	def getAll(self):
		cm = ConnectionManager('KappaBase')
		res = cm.executeSQL("SELECT * FROM Vector")
		vectorList = []
		for elem in res:
			vectorList.append(VectorModel(elem[0], elem[1], "tagname", "parent"))
		return vectorList

	def getById(self, id):
		cm = ConnectionManager('KappaBase')
		res = cm.executeSQL("SELECT * FROM Vector WHERE id_vector="+str(id))
		if (len(res)!=1) : 
			return
		res2 = VectorModel(res[0][0], res[0][1], "tagname", "parent")
		return res2

	def update(self, vectorModel):
		cm = ConnectionManager('KappaBase')
		res = cm.executeAndCommitSQL("UPDATE Vector SET value_vector=\"" + str(vectorModel.value) + "\" WHERE id_vector=" + str(vectorModel.id))

	def create(self, vectorModel):
		cm = ConnectionManager('KappaBase')
		res = cm.executeAndCommitSQL("INSERT INTO Vector (id_vector, value_vector) VALUES (" + str(vectorModel.id) + ", \"" + vectorModel.value + "\")")
