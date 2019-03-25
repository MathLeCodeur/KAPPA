"""
Affichage d'une seule photo avec ses métadonnées associées.

Les visages et les objets détectés sur l'image sont encadrés lors du clic sur le bouton "Encadrer
les objets".
"""

import os

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from ui.dependencies import *
from ui.generated.photo_viewer_panel_ui import *
from ui.widgets.aspect_ratio_image import *

class PhotoViewerPanel(QWidget):
    def __init__(self, parent: QWidget = None):
        super(PhotoViewerPanel, self).__init__(parent)

        self.__ui = Ui_PhotoViewerPanel()
        self.__ui.setupUi(self)

        #self.__faceDetector = TensoflowFaceDector()

    def setPhoto(self, photo: Photo):
        pixmap = QPixmap(photo.path)

        self.__ui.image.setPixmap(pixmap)
        #self.__ui.image.setDetectionBoxes(self.__faceDetector.getBoxes(photo.path))
        self.__ui.nameValueLabel.setText(os.path.basename(photo.path))
        self.__ui.sizeValueLabel.setText(str(round(os.path.getsize(photo.path) / 1000, 1)) + ' KB')
        self.__ui.dimensionsValueLabel.setText(str(pixmap.width()) + 'x' + str(pixmap.height()))
        self.__ui.dateValueLabel.setText('Inconnue' if photo.date is None else photo.date.strftime("%d/%m/%Y"))
        self.__ui.placeValueLabel.setText('Inconnu' if photo.place is None else photo.place)

        self.__clearLayout(self.__ui.classifications)

        for classification in photo.classifications:
            self.__ui.classifications.addWidget(QLabel(classification))
        else:
            self.__ui.classifications.addWidget(QLabel('Aucune classification'))

    @pyqtSlot(name='on_backButton_clicked')
    def returnToPhotoGallery(self):
        self.window().setActivePanel(self.window().getPhotoGalleryPanel())

    def __clearLayout(self, layout: QLayout):
        for i in reversed(range(layout.count())):
            layout.itemAt(i).widget().setParent(None)
