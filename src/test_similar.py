

from kappa.controllers.ImageController import ImageController



import os
import glob
from PIL import Image
import time

def main():

    print("research SIMILAR ...")
    imgCtl = ImageController()
    
    rows = imgCtl.getAll()
    j=0
    for row in rows:
        j+=1
        for tag in row.objectVectors :
            print("my image ",j," ",tag)


if __name__ == "__main__":
    main()
