import ConnectionManager
from VectorDAO import VectorDAO
from ImageDAO import ImageDAO
from ImageController import ImageController

def main():
	 #y = ConnectionManager.ConnectionManager('KappaBase.db')
	#print(y.instance.connection)

	#Select
	#rows = y.executeSQL('select * from Vector');
	imgCtl = ImageController()
	rows = imgCtl.getAll()
	print(rows)
	for row in rows:
		print(str(row.path))
	#print("Image : "+str(rows[0].path))
	#print("Image : "+str(rows[1].path))
	#for elem in rows:
	#	print(row)
	#y.executeAndCommitSQL("Insert into Image (id_image) values (3)")

if __name__ == "__main__":
    main()
