from kappa.dao.DAO import DAO
from kappa.dao.VectorDAO import VectorDAO
from kappa.dao import ConnectionManager
from kappa.models.VectorModel import VectorModel
from kappa.models.ObjectVectorModel import ObjectVectorModel



class ObjectVectorDAO(DAO):
	def __init__(self):
		super(ObjectVectorDAO, self).__init__()

	def update(self, objectVectorModel):
		cm = ConnectionManager.ConnectionManager('KappaBase')
		vDao = VectorDAO()
		vDao.update(VectorModel(objectVectorModel.id, objectVectorModel.value, objectVectorModel.tagName))
		if(objectVectorModel.parent!=None) :
			cm.executeAndCommitSQL("UPDATE Object_vector SET id_parent=" + str(objectVectorModel.parent.id)+ " WHERE id_vector=" + str(objectVectorModel.id))
		else :
			cm.executeAndCommitSQL("UPDATE Object_vector SET id_parent=NULL WHERE id_vector=" + str(objectVectorModel.id))

	def create(self, objectVectorModel):
		cm = ConnectionManager.ConnectionManager('KappaBase')
		vDao = VectorDAO()
		vDao.create(VectorModel(objectVectorModel.id, objectVectorModel.value, objectVectorModel.tagName))
		if(objectVectorModel.parent!=None) :
			res = cm.executeAndCommitSQL("INSERT INTO Object_vector (id_vector, id_parent) VALUES (" + str(objectVectorModel.id) + ", " + str(objectVectorModel.parent.id) + ")")
		else :
			res = cm.executeAndCommitSQL("INSERT INTO Object_vector (id_vector) VALUES (" + str(objectVectorModel.id) + ")")

	def getByImageId(self, id):
		cm = ConnectionManager.ConnectionManager('KappaBase.db')
		res = cm.executeSQL("select * from Vector NATURAL JOIN OBJECT_VECTOR NATURAL JOIN INCLUDE where id_image = "+str(id)+";")
		vectorList = []
		for elem in res:
			if(elem[3]!=None) :
				vectorList.append(ObjectVectorModel(elem[0], elem[1], elem[2], self.getById(elem[3])))
			else :
				vectorList.append(ObjectVectorModel(elem[0], elem[1], elem[2], None))
		return vectorList

	def getAll(self):
		cm = ConnectionManager.ConnectionManager('KappaBase')
		res = cm.executeSQL("SELECT * FROM Vector NATURAL JOIN Object_vector)")
		vectorList = []
		for elem in res:
			if(elem[3]!=None) :
				vectorList.append(ObjectVectorModel(elem[0], elem[1], elem[2], self.getById(elem[3])))
			else :
				vectorList.append(ObjectVectorModel(elem[0], elem[1], elem[2], None))
		return vectorList

	def getById(self, id):
		cm = ConnectionManager.ConnectionManager('KappaBase')
		res = cm.executeSQL("SELECT * FROM Vector NATURAL JOIN Object_vector WHERE id_vector=" + str(id))
		if (len(res)!=1) :
			return
		if(res[0][3]!=None) :
			res2 = ObjectVectorModel(res[0][0], res[0][1], res[0][2], self.getById(res[0][3]))
		else :
			res2 = ObjectVectorModel(res[0][0], res[0][1], res[0][2], None)
		return res2

	def delete(self,objVectorModel):
		cm = ConnectionManager.ConnectionManager('KappaBase')
		vDao = VectorDAO()
		vDao.delete(VectorModel(objVectorModel.id, objVectorModel.value, objVectorModel.tagName))
		cm.executeAndCommitSQL("Delete from object_vector WHERE id_vector=" + str(objVectorModel.id))

	def getByValue(self, value):
		cm = ConnectionManager.ConnectionManager('KappaBase')
		res = cm.executeSQL("SELECT * FROM Vector NATURAL JOIN Object_vector WHERE value_vector=\"" + value + "\"")
		if (len(res)!=1) :
			return
		if(res[0][3]!=None) :
			res2 = ObjectVectorModel(res[0][0], res[0][1], res[0][2], self.getById(res[0][3]))
		else :
			res2 = ObjectVectorModel(res[0][0], res[0][1], res[0][2], None)
		return res2

	def getNextId(self):
		cm = ConnectionManager.ConnectionManager('KappaBase')
		res = cm.executeSQL("SELECT MAX(id_vector) FROM Vector")
		res2 = res
		for elem in res:
			if(elem[0] == None):
				res2=0
				break
			res2=elem[0]+1
		return res2

	def importObjectVectors(self, tagItems):
		cm = ConnectionManager.ConnectionManager('KappaBase')

		for vector, tags_and_parent in tagItems:
			#exemple :
			#vector          => 'n07877187'
			#tags_and_parent => ('spaghetti and meatballs', 'n07557434')

			vChild = self.getByValue(vector)

			if (vChild!=None) :
				vChild.value = vector
				vChild.tagName = tags_and_parent[0]
				if(tags_and_parent[1]==None) :
					vChild.parent = None
				else :
					vParent = self.getByValue(tags_and_parent[1])
					if(vParent!=None) :
						vChild.parent = vParent
					else :
						nextId=self.getNextId()
						vParent = ObjectVectorModel(nextId, tags_and_parent[1], "", None)
						vChild.parent = vParent
						self.create(vParent)
				self.update(vChild)
			else :
				nextId=self.getNextId()
				vChild = ObjectVectorModel(nextId, vector, tags_and_parent[0], None)
				if(tags_and_parent[1]==None) :
					vChild.parent = None
				else :
					vParent = self.getByValue(tags_and_parent[1])
					if(vParent!=None) :
						vChild.parent = vParent
					else :
						vParent = ObjectVectorModel(nextId+1, tags_and_parent[1], "", None)
						vChild.parent = vParent
						self.create(vParent)
				self.create(vChild)
