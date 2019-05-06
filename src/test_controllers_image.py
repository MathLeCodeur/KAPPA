from kappa.dao.ConnectionManager import ConnectionManager
from kappa.dao.VectorDAO import VectorDAO
from kappa.dao.ObjectVectorDAO import ObjectVectorDAO
from kappa.controllers.ObjectVectorController import ObjectVectorController
from kappa.controllers.ImageController import ImageController

import os
import glob
from PIL import Image
import time

def main():
	y = ConnectionManager('KappaBase.db')
	x = ConnectionManager('KappaBase.db')
	print("test singleton")
	print(y.instance.connection == x.instance.connection)

	imgCtl = ImageController()
	rows = imgCtl.getAll()
	i=0
	for row in rows:
		i+=1

	rows = imgCtl.getAllOrderByDate()
	j=0
	for row in rows:
		j+=1
	print("test byDate and all")
	print(j==i)
	#imgCtl.importImageFolder("/home/kappa/Documents/Image/")

if __name__ == "__main__":
    main()
