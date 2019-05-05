from kappa.dao.DAO import DAO
from kappa.dao import ConnectionManager
from kappa.models.VectorModel import VectorModel



class ObjectVectorDAO(DAO):
	def __init__(self):        
		super(ObjectVectorDAO, self).__init__()

	def getAll(self):
		cm = ConnectionManager.ConnectionManager('KappaBase')
		res = cm.executeSQL("SELECT * FROM Vector WHERE id_vector IN (SELECT id_vector from Object_vector)")
		vectorList = []
		for elem in res: 
			vectorList.append(VectorModel(elem[0], elem[1], "tagname", "parent"))
		return vectorList

	def getById(self, id):
		cm = ConnectionManager.ConnectionManager('KappaBase')
		res = cm.executeSQL("SELECT * FROM Vector WHERE id_vector=" + str(id) + " AND id_vector IN (SELECT id_vector from Object_vector)")
		if (len(res)!=1) : 
			return
		res2 = VectorModel(res[0][0], res[0][1], "tagname", "parent")
		return res2
	
	def getByValue(self, value):
		cm = ConnectionManager.ConnectionManager('KappaBase')
		res = cm.executeSQL("SELECT * FROM Vector WHERE value_vector='" + value + "' AND id_vector IN (SELECT id_vector from Object_vector)")
		if (len(res)!=1) : 
			return
		res2 = VectorModel(res[0][0], res[0][1], "tagname", "parent")
		return res2

	def update(self, vectorModel):
		cm = ConnectionManager.ConnectionManager('KappaBase')
		res = cm.executeAndCommitSQL("UPDATE Vector SET value_vector=\"" + str(vectorModel.value) + "\" WHERE id_vector=" + str(vectorModel.id) + " AND id_vector IN (SELECT id_vector from Object_vector)")

	def create(self, vectorModel):
		cm = ConnectionManager.ConnectionManager('KappaBase')
		res = cm.executeAndCommitSQL("INSERT INTO Vector (id_vector, value_vector) VALUES (" + str(vectorModel.id) + ", \"" + vectorModel.value + "\")")
		res = cm.executeAndCommitSQL("INSERT INTO Object_vector (id_vector) VALUES (" + str(vectorModel.id) + ")")

	def getNextId(self):
		cm = ConnectionManager.ConnectionManager('KappaBase')
		res = cm.executeSQL("SELECT MAX(id_vector) FROM VECTOR")
		res2 = res
		for elem in res:
			if(elem[0] == None):
				res2=0
				break
			res2=elem[0]+1
		
		return res2
