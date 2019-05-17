

from kappa.controllers.ImageController import ImageController



import os
import glob
from PIL import Image
import time

def main():

    print("research SIMILAR ...")
    imgCtl = ImageController()
    listimgBase = imgCtl.getAll()
    imgBase = listimgBase[4]
    print(imgBase, " compare to", imgBase.path)
    
    listSimilar = imgCtl.searchSimilar(imgBase)
    
    
    for img in listSimilar:
        print("similar to ",img.path)


if __name__ == "__main__":
    main()
