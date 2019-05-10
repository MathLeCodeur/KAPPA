import kappa.dao.DAO as dao
import kappa.controllers.Controller as ctl
from kappa.dao import ConnectionManager
from kappa.models.FaceVectorModel import FaceVectorModel
from kappa.dao.FaceVectorDAO import FaceVectorDAO
from kappa.face_detection.inference_image_face import *
from kappa.face_recognition.face_recognition import *
import os
import glob
from PIL import Image
import time
import face_recognition
import scipy.misc
import pickle
import codecs

class FaceVectorController(ctl.Controller):
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

    def loadRecognizedPeopleFaceVector(self, faceDetector: TensorflowFaceDetector):
        pass

    def getRecognizedPeople(self, imagePath: str, faceDetector: TensorflowFaceDetector):
        faceBoxes = faceDetector.getBoxes(imagePath)
        peopleInformation = [[faceVectorModel.tagName, pickle.loads(codecs.decode(faceVectorModel.value.encode(), "base64"))] for faceVectorModel in self.getKnown()]
        names = recognizePeople(peopleInformation, faceBoxes, imagePath)

        imageMatrix = face_recognition.load_image_file(imagePath)
        imageHeight, imageWidth, _ = imageMatrix.shape

        tagData = []

        for i in range(len(names)):
            currentPersonPicture = imageMatrix[int(round(faceBoxes[i][0] * imageHeight)) : int(round(faceBoxes[i][2] * imageHeight)),
                        int(round(faceBoxes[i][1] * imageWidth)) : int(round(faceBoxes[i][3] * imageWidth))]

            if face_recognition.face_encodings(currentPersonPicture):
                tagData.append({'name': names[i], 'boundingBox': faceBoxes[i]})

        return tagData

    def commitFaceVectorChange(self, oldTagName, newTagName, croppedImagePath):
        if oldTagName == 'Unknown':
            if newTagName != 'Unknown' and newTagName:
                print('create')
                imageMatrix = face_recognition.load_image_file(croppedImagePath)

                faceEncodings = face_recognition.face_encodings(imageMatrix)
                if faceEncodings:
                    faceVector = faceEncodings[0]
                    base64FaceVector = codecs.encode(pickle.dumps(faceVector), "base64").decode()

                    self.cDao.create(FaceVectorModel(self.cDao.getNextId(), base64FaceVector, newTagName, True))
        else:
            if newTagName and newTagName != 'Unknown':
                print('update')
            else:
                print('delete')
