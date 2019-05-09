from kappa.controllers.ImageController import ImageController

def main():
	imgCtl = ImageController()
	path = "/home/kappa/Documents/Image/"
	imgCtl.importImageFolder(path)

if __name__ == "__main__":
    main()
