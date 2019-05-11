"""
Affichage d'une seule photo avec ses métadonnées associées.

Les visages et les objets détectés sur l'image sont encadrés lors du clic sur le bouton "Encadrer
les objets".
"""

import os

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import config
from kappa.models.ImageModel import *
from kappa.ui.generated.photo_viewer_panel_ui import *

class PhotoViewerPanel(QWidget):
    def __init__(self, parent: QWidget = None):
        super(PhotoViewerPanel, self).__init__(parent)

        self.__ui = Ui_PhotoViewerPanel()
        self.__ui.setupUi(self)

        self.__drawRecognizedPeopleAndObjects = config.get('frameObjects')

    def setPhoto(self, photo: ImageModel):
        pixmap = QPixmap(photo.path)

        self.__photoPath = photo.path

        self.__ui.image.setPixmap(pixmap)
        self.__ui.imageNameValueLabel.setText(os.path.basename(photo.path))
        self.__ui.imageDateValueLabel.setText('---' if photo.creation_date is None else photo.creation_date)
        self.__ui.imageSizeValueLabel.setText(str(round(os.path.getsize(photo.path) / 1000, 1)) + ' KB')
        self.__ui.imageDimensionsValueLabel.setText(str(pixmap.width()) + 'x' + str(pixmap.height()))
        self.__ui.imagePathValueLabel.setText(photo.path)

        self.__clearTags(self.__ui.imageTagsContainer)

        tags = sorted([vector.tagName for vector in photo.faceVectors + photo.objectVectors])

        for tag in tags:
            self.__ui.imageTagsContainer.addWidget(QLabel(tag))
        else:
            self.__ui.imageTagsContainer.addWidget(QLabel("---"))

        self.updateRecognizedPeopleAndObjects()

    def updateRecognizedPeopleAndObjects(self):
        if self.__drawRecognizedPeopleAndObjects:
            self.__ui.frameObjectsAndPeopleActionButton.setStyleSheet('QPushButton{ border-bottom: 4px solid ' + config.get('themeColor') + '; }')
            recognizedPeople = self.window().faceVectorController.getRecognizedPeople(self.__photoPath, self.window().faceDetector)
            self.__ui.image.setRecognizedPeopleAndObjects(recognizedPeople)
        else:
            self.__ui.image.saveTagData()
            self.__ui.image.setRecognizedPeopleAndObjects([])
            self.__ui.frameObjectsAndPeopleActionButton.setStyleSheet('')

    @pyqtSlot(name='on_backActionButton_clicked')
    def returnToPhotoGallery(self):
        self.__ui.image.saveTagData()
        self.window().setActivePanel(self.window().getPhotoGalleryPanel())

    @pyqtSlot(name='on_frameObjectsAndPeopleActionButton_clicked')
    def toggleFrameObjectsAndPeople(self):
        self.__drawRecognizedPeopleAndObjects = not self.__drawRecognizedPeopleAndObjects
        self.updateRecognizedPeopleAndObjects()
        config.set('frameObjects', self.__drawRecognizedPeopleAndObjects)

    def __clearTags(self, layout: QLayout):
        for i in reversed(range(1, layout.count())):
            layout.itemAt(i).widget().setParent(None)
