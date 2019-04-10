import ConnectionManager
import os
import glob
from PIL import Image
import time

def main():
	y = ConnectionManager.ConnectionManager('KappaBase.db')
	print(y.instance.connection)
	l=os.listdir("/home/kappa/Documents/Image/")
	ui=y.executeSQL("select Max(id_image) from Image");
	u=ui
	for elem in ui:
		u=elem[0]+1
	#print(ui)
	for i in l:
		im = Image.open("/home/kappa/Documents/Image/"+str(i))
		path = "/home/kappa/Documents/Image/"+str(i)
		size = os.path.getsize(path)
		width = im.size[0]
		height = im.size[1]
		date = str(time.ctime(os.path.getctime("/home/kappa/Documents/Image/"+str(i))))
		sql = "Insert into IMAGE (id_image,creation_date ,length, width,size, path) values ("+str(u)+",'"+date+"',"+str(height)+", "+str(width)+ ", " +str(size)+", '" +path+"')"
		print(sql)
		y.executeAndCommitSQL(sql)
		u+=1

if __name__ == "__main__":
    main()
