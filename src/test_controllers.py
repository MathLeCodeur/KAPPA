import kappa.dao.ConnectionManager
from kappa.dao.VectorDAO import VectorDAO
from kappa.dao.ObjectVectorDAO import ObjectVectorDAO
from kappa.controllers.ObjectVectorController import ObjectVectorController
import os
import glob
from PIL import Image
import time

def main():
	 #y = ConnectionManager.ConnectionManager('KappaBase.db')
	#print(y.instance.connection)

	#Select
	#rows = y.executeSQL('select * from Vector');
	imgCtl = ObjectVectorController()
	#rows = imgCtl.getAll()
	#print(rows)
	#for row in rows:
	#	print(str(row.path))

	imgCtl.importObjectVectors()

	#imgCtl.importImageFolder("/home/kappa/Documents/Image/")
	#print("Image : "+str(rows[0].path))
	#print("Image : "+str(rows[1].path))
	#for elem in rows:
	#	print(row)
	#y.executeAndCommitSQL("Insert into Image (id_image) values (3)")

if __name__ == "__main__":
    main()
