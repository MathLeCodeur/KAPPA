

from kappa.controllers.ImageController import ImageController



import os
import glob
from PIL import Image
import time

def main():

    print("research TAG ...")
    Imctrl = ImageController()
    resTag = Imctrl.searchTags("./res/images/samples/image3.jpg")

    for name , score in resTag.items():
        print('%s (score = %.5f)' % (name, score))

    #print('res = ',resTag)
    #imgCtl.coucou()


if __name__ == "__main__":
    main()
