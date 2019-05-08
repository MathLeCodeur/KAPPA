from kappa.dao.ConnectionManager import ConnectionManager
from kappa.dao.VectorDAO import VectorDAO
from kappa.dao.FaceVectorDAO import FaceVectorDAO
from kappa.models.FaceVectorModel import FaceVectorModel
from kappa.controllers.FaceVectorController import FaceVectorController
from kappa.controllers.ObjectVectorController import ObjectVectorController
from kappa.controllers.ImageController import ImageController

import os
import glob
from PIL import Image
import time

def main():
    fVecCtl = FaceVectorController()
    rows = fVecCtl.getAll()
    for row in rows:
	    print(str(row.id)+" "+str(row.value)+" "+ str(row.isKnown))

    fVector = FaceVectorModel(999, "value 999", "tag 999", 0)
    #fVecCtl.create(fVector)

    rows = fVecCtl.getAll()
    for row in rows:
	    print(str(row.id)+" "+str(row.value)+" "+ str(row.isKnown))

    row = fVecCtl.getById(999)
    print(str(row.id)+" "+str(row.value)+" "+ str(row.isKnown))

    row = fVecCtl.getByValue("value vector10")
    print(str(row.id)+" "+str(row.value)+" "+ str(row.isKnown))

    rows = fVecCtl.getByImageId(5)
    print("test by image id")
    for row in rows:
	    print(str(row.id)+" "+str(row.value)+" "+ str(row.isKnown))

    oVecCtl = ObjectVectorController()
    print("test obj by image id")

    rows = oVecCtl.getByImageId(7)
    for row in rows:
        print(str(row.id)+" "+str(row.value))



if __name__ == "__main__":
    main()
