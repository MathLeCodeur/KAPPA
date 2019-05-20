"""
Affichage d'une seule photo avec ses métadonnées associées.

Les visages et les objets détectés sur l'image sont encadrés lors du clic sur le bouton "Encadrer
les objets".
"""

import functools
import os

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import config
from kappa.models.ImageModel import *
from kappa.ui.generated.photo_viewer_panel_ui import *
from kappa.ui.widgets.aspect_ratio_image import *
from kappa.ui.widgets.photo_view import *

class PhotoViewerPanel(QWidget):
    def __init__(self, parent: QWidget = None):
        super(PhotoViewerPanel, self).__init__(parent)

        self.__ui = Ui_PhotoViewerPanel()
        self.__ui.setupUi(self)

        self.__ui.scrollAreaSimilarImages.setVisible(False)

        self.__drawRecognizedPeopleAndObjects = config.get('frameObjects')

    def setPhoto(self, photo: ImageModel):
        pixmap = QPixmap(photo.path)

        self.__imageModel = photo

        self.__ui.image.setPixmap(pixmap)
        self.__ui.imageNameValueLabel.setText(os.path.basename(photo.path))
        self.__ui.imageDateValueLabel.setText('---' if photo.creation_date is None else photo.creation_date)
        self.__ui.imageSizeValueLabel.setText(str(round(os.path.getsize(photo.path) / 1000, 1)) + ' KB')
        self.__ui.imageDimensionsValueLabel.setText(str(pixmap.width()) + 'x' + str(pixmap.height()))
        self.__ui.imagePathValueLabel.setText(photo.path)

        self.__clearLayout(self.__ui.imageTagsContainer)

        tags = photo.getObjectVectorsWithTheirMommiesAndDaddies()
        formattedTags = [tag.replace('/', ' > ').title() for tag in tags]
        shortenedFormattedTags = [' > '.join(tag.split(' > ')[-2:]) for tag in formattedTags]

        if len(shortenedFormattedTags) != 0:
            for tag in shortenedFormattedTags:
                self.__ui.imageTagsContainer.addWidget(QLabel(tag))
        else:
            self.__ui.imageTagsContainer.addWidget(QLabel("---"))

        self.updateRecognizedPeopleAndObjects()

    def updateRecognizedPeopleAndObjects(self):
        if self.__drawRecognizedPeopleAndObjects:
            self.__ui.frameObjectsAndPeopleActionButton.setStyleSheet('QPushButton{ border-bottom: 4px solid ' + config.get('themeColor') + '; }')
            recognizedPeople = self.window().faceVectorController.getRecognizedPeople(self.__imageModel.path)
            self.__ui.image.setRecognizedPeopleAndObjects(recognizedPeople)
        else:
            self.__ui.image.saveTagData(self.__imageModel.path)
            self.__ui.image.setRecognizedPeopleAndObjects([])
            self.__ui.frameObjectsAndPeopleActionButton.setStyleSheet('')

    @pyqtSlot(name='on_backActionButton_clicked')
    def returnToPhotoGallery(self):
        self.__ui.image.saveTagData(self.__imageModel.path)
        self.window().setActivePanel(self.window().getPhotoGalleryPanel())

    @pyqtSlot(name='on_frameObjectsAndPeopleActionButton_clicked')
    def toggleFrameObjectsAndPeople(self):
        self.__drawRecognizedPeopleAndObjects = not self.__drawRecognizedPeopleAndObjects
        self.updateRecognizedPeopleAndObjects()
        config.set('frameObjects', self.__drawRecognizedPeopleAndObjects)

    @pyqtSlot(name='on_searchSimilarActionButton_clicked')
    def toggleShowSimilarImages(self):
        if not self.__ui.similarImagesContainer.isVisible():
            self.__clearLayout(self.__ui.similarImagesLayout)
            similarImages = self.window().imageController.searchSimilar(self.__imageModel)

            for similarImage in similarImages:
                similarImageWidget = AspectRatioImage()
                similarImageWidget.setPixmap(QPixmap(similarImage.path))
                similarImageWidget.mousePressEvent = functools.partial(self.__openPhoto, similarImage)
                self.__ui.similarImagesLayout.addWidget(similarImageWidget)

            if similarImages:
                self.__ui.scrollAreaSimilarImages.setVisible(True)

        else:
            self.__ui.scrollAreaSimilarImages.setVisible(False)

    def __openPhoto(self, image: ImageModel, param):
        self.setPhoto(image)

    def __clearLayout(self, layout: QLayout):
        for i in reversed(range(0, layout.count())):
            layout.itemAt(i).widget().setParent(None)
