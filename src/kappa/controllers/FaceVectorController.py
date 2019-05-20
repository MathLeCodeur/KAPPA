from kappa.controllers.Controller import Controller
from kappa.dao import ConnectionManager
from kappa.models.FaceVectorModel import FaceVectorModel
from kappa.dao.FaceVectorDAO import FaceVectorDAO
from kappa.face_recognition.face_recognition import *
import face_recognition
import pickle
import codecs
from typing import *

class FaceVectorController(Controller):
    def __init__(self):
        super().__init__()
        self.cDao = FaceVectorDAO()

    def create(self,fVectorModel):
        self.cDao.create(fVectorModel)

    def getAll(self):
        return self.cDao.getAll()

    def getById(self, id):
        return self.cDao.getById(id)

    def getKnown(self):
        return self.cDao.getKnown()

    def getByValue(self, value):
        return self.cDao.getByValue(value)

    def getByImageId(self, id):
        return self.cDao.getByImageId(id)

    def getRecognizedPeople(self, imagePath: str):
        imageMatrix = face_recognition.load_image_file(imagePath)
        peopleInformation = [[faceVectorModel.tagName, pickle.loads(codecs.decode(faceVectorModel.value.encode(), "base64"))] for faceVectorModel in self.getKnown()]

        faceBoxes = face_recognition.face_locations(imageMatrix)
        names = recognizePeople(peopleInformation, faceBoxes, imageMatrix)

        return [{'name': names[i], 'boundingBox': faceBoxes[i]} for i in range(len(faceBoxes))]

    def commitFaceVectorChange(self, oldTagName: str, newTagName: str, imagePath: str, faceBox: Tuple[int, int, int, int]):
        if oldTagName == 'Unknown':
            if newTagName != 'Unknown' and newTagName:
                print('create')
                imageMatrix = face_recognition.load_image_file(imagePath)

                faceEncodings = face_recognition.face_encodings(imageMatrix, known_face_locations=[faceBox])
                faceVector = faceEncodings[0]
                base64FaceVector = codecs.encode(pickle.dumps(faceVector), "base64").decode()

                self.cDao.create(FaceVectorModel(self.cDao.getNextId(), base64FaceVector, newTagName, True))
        else:
            if newTagName and newTagName != 'Unknown':
                print('update')
            else:
                print('delete')
