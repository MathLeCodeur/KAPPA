import kappa.dao.DAO as dao
from kappa.dao import ConnectionManager
import kappa.models.ImageModel as im



class ImageDAO(dao.DAO):
	def __init__(self):
		super().__init__()

	def getAllOrderByDate(self):
		cm = ConnectionManager.ConnectionManager('KappaBase.db')
		res = cm.executeSQL("SELECT * FROM Image order by creation_date")
		imageList = []
		for elem in res:
			#print(elem)
			#sqlObject = cm.executeSQL("select * from Vector v, object_vector fv where v.id_vector=fv.id_vector and v.id_vector in (select id_vector from INCLUDE where id_image="+elem[0]+")")
			#sqlFace = cm.executeSQL("select * from Vector v, Face_vector fv where v.id_vector=fv.id_vector and v.id_vector in (select id_vector from INCLUDE where id_image="+elem[0]+")")

			#select * from Vector v, Face_vector fv where v.id_vector=fv.id_vector and v.id_vector in (select id_vector from INCLUDE where id_image=1);
			imageList.append(im.ImageModel(elem[0], elem[1],elem[2],elem[3],elem[4],elem[5],elem[6], "face", "obj"))
		return imageList

	def getAll(self):
		cm = ConnectionManager.ConnectionManager('KappaBase.db')
		res = cm.executeSQL("SELECT * FROM Image")
		imageList = []
		for elem in res:
			#print(elem)
			#sqlObject = cm.executeSQL("select * from Vector v, object_vector fv where v.id_vector=fv.id_vector and v.id_vector in (select id_vector from INCLUDE where id_image="+elem[0]+")")
			#sqlFace = cm.executeSQL("select * from Vector v, Face_vector fv where v.id_vector=fv.id_vector and v.id_vector in (select id_vector from INCLUDE where id_image="+elem[0]+")")

			#select * from Vector v, Face_vector fv where v.id_vector=fv.id_vector and v.id_vector in (select id_vector from INCLUDE where id_image=1);
			imageList.append(im.ImageModel(elem[0], elem[1],elem[2],elem[3],elem[4],elem[5],elem[6], "face", "obj"))
		return imageList

	def getById(self,id):
		cm = ConnectionManager.ConnectionManager('KappaBase.db')
		res = cm.executeSQL("SELECT * FROM Image where id_image ="+id+";")
		return res

	def getNextId(self):
		cm = ConnectionManager.ConnectionManager('KappaBase')
		res = cm.executeSQL("SELECT MAX(id_image) FROM IMAGE")
		res2 = res
		for elem in res:
			if(elem[0] == None):
				res2=0
				break
			res2=elem[0]+1

		return res2
	#d_image INT PRIMARY KEY NOT NULL,
	#comment VARCHAR(255),
	#creation_date date,
	#length int,
	#width int,
	#size int,
	#path VARCHAR(255)
	def update(self, imageMod):
		print("update")


	def create(self, imgModel):
		print("create")
		cm = ConnectionManager.ConnectionManager('KappaBase.db')
		res = cm.executeAndCommitSQL("INSERT INTO Image (id_image, comment,creation_date,length,width,size,path) VALUES (" + imgModel.id + ", \"" + imgModel.comment + "\""+imgModel.creation_date+", "+imgModel.length+","+imgModel.size+","+imgModel.path+")")
