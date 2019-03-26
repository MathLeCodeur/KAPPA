import ConnectionManager
import os
import glob

def main():
	l=os.listdir("/home/kappa/Documents/Image/")
	for i in l:
		print(i+" s; "+str(os.path.getsize("/home/kappa/Documents/Image/"+str(i))))
	#y = ConnectionManager.ConnectionManager('../KappaBase.db')
	#print(y.instance.connection)

	#Select
	#rows = y.executeSQL('select * from Image');
	#for row in rows:
	#	print(row)
	#y.executeAndCommitSQL("Insert into Image (id_image) values (3)")

if __name__ == "__main__":
    main()
