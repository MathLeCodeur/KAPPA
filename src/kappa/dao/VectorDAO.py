from kappa.dao.DAO import DAO as daoclass
from kappa.dao.ConnectionManager import ConnectionManager
from kappa.models.VectorModel import VectorModel



class VectorDAO(daoclass):
	def __init__(self):
		super(VectorDAO, self).__init__()

	def getAll(self):
		cm = ConnectionManager('KappaBase')
		res = cm.executeSQL("SELECT * FROM Vector")
		vectorList = []
		for elem in res:
			vectorList.append(VectorModel(elem[0], elem[1], elem[2]))
		return vectorList

	def getById(self, id):
		cm = ConnectionManager('KappaBase')
		res = cm.executeSQL("SELECT * FROM Vector WHERE id_vector="+str(id))
		if (len(res)!=1) :
			return
		res2 = VectorModel(res[0][0], res[0][1], elem[0][2])
		return res2

	def update(self, vectorModel):
		cm = ConnectionManager('KappaBase')
		res = cm.executeAndCommitSQL("UPDATE Vector SET value_vector=\"" + str(vectorModel.value) + "\" , tag_name=\"" + str(vectorModel.tagName) + "\" WHERE id_vector=" + str(vectorModel.id))

	def delete(self,vectorModel):
		cm = ConnectionManager('KappaBase')
		res = cm.executeAndCommitSQL("Delete from include WHERE id_vector=" + str(vectorModel.id))
		res = cm.executeAndCommitSQL("Delete from Vector WHERE id_vector=" + str(vectorModel.id))

	def create(self, vectorModel):
		cm = ConnectionManager('KappaBase')
		res = cm.executeAndCommitSQL("INSERT INTO Vector (id_vector, value_vector, tag_name) VALUES (" + str(vectorModel.id) + ", \"" + vectorModel.value + "\", \"" + vectorModel.tagName + "\")")

	def updateWithoutCommit(self, vectorModel):
		cm = ConnectionManager('KappaBase')
		res = cm.executeSQL("UPDATE Vector SET value_vector=\"" + str(vectorModel.value) + "\" , tag_name=\"" + str(vectorModel.tagName) + "\" WHERE id_vector=" + str(vectorModel.id))

	def createWithoutCommit(self, vectorModel):
		cm = ConnectionManager('KappaBase')
		res = cm.executeSQL("INSERT INTO Vector (id_vector, value_vector, tag_name) VALUES (" + str(vectorModel.id) + ", \"" + vectorModel.value + "\", \"" + vectorModel.tagName + "\")")
