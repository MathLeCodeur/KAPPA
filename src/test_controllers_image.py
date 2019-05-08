from kappa.dao.ConnectionManager import ConnectionManager
from kappa.dao.VectorDAO import VectorDAO
from kappa.dao.ObjectVectorDAO import ObjectVectorDAO
from kappa.controllers.ObjectVectorController import ObjectVectorController
from kappa.controllers.ImageController import ImageController
from kappa.controllers.FaceVectorController import FaceVectorController

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

	print("test link")
	fVecCtl = FaceVectorController()
	v = fVecCtl.getById(9)
	print(str(v.id)+" "+str(v.value)+" "+ str(v.isKnown))
	imgCtl.linkToVector(rows[0], v)

if __name__ == "__main__":
    main()
