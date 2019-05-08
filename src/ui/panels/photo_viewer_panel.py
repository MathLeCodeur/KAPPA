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
        self.__ui.imageNameValueLabel.setText(os.path.basename(photo.path))
        self.__ui.imageDateValueLabel.setText('---' if photo.date is None else photo.date.strftime("%d/%m/%Y"))
        self.__ui.imagePlaceValueLabel.setText('---' if photo.place is None else photo.place)
        self.__ui.imageSizeValueLabel.setText(str(round(os.path.getsize(photo.path) / 1000, 1)) + ' KB')
        self.__ui.imageDimensionsValueLabel.setText(str(pixmap.width()) + 'x' + str(pixmap.height()))
        self.__ui.imagePathValueLabel.setText(photo.path)

        self.__clearTags(self.__ui.imageTagsContainer)

        for tag in photo.classifications:
            print(tag)
            self.__ui.imageTagsContainer.addWidget(QLabel(tag))
        else:
            self.__ui.imageTagsContainer.addWidget(QLabel("---"))

    @pyqtSlot(name='on_backActionButton_clicked')
    def returnToPhotoGallery(self):
        self.window().setActivePanel(self.window().getPhotoGalleryPanel())

    def __clearTags(self, layout: QLayout):
        for i in reversed(range(1, layout.count())):
            layout.itemAt(i).widget().setParent(None)
