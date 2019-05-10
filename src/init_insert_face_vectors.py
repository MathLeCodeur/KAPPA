import os

from kappa.face_recognition.face_recognition import *
from kappa.controllers.FaceVectorController import *
from kappa.dao.FaceVectorDAO import *
from kappa.models.FaceVectorModel import *

def main():
    faceVectorController = FaceVectorController()
    faceVectorDAO = FaceVectorDAO()
    known_image3 = face_recognition.load_image_file("/home/kappa/Bureau/Lucie Gartiser.jpg")

    recognizedPeopleDir = os.path.join('res', 'images', 'recognized_people')

    for recognizedPersonFile in os.listdir(recognizedPeopleDir):
        recognizedPersonName = recognizedPersonFile.split(".")[0]
        faceVectorController.create(FaceVectorModel(faceVectorDAO.getNextId(), None, recognizedPersonName, True))

if __name__ == '__main__':
    main()
