from kappa.controllers.Controller import Controller
from kappa.dao import ConnectionManager
from kappa.models.FaceVectorModel import FaceVectorModel
from kappa.dao.FaceVectorDAO import FaceVectorDAO
import os
import glob
from PIL import Image
import time

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

    def getByValue(self, value):
        return self.cDao.getByValue(value)

    def getByImageId(self, id):
        return self.cDao.getByImageId(id)
