"""
Widget permettant d'afficher une liste de photos.
"""

from typing import *

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from ui.dependencies import *
from ui.widgets.flow_layout import *

class PhotoListView(QWidget):
    def __init__(self, parent: QWidget = None):
        super(PhotoListView, self).__init__(parent)

        self.__layout = FlowLayout(self, 30, 16, 16)
        self.setLayout(self.__layout)

    def setPhotos(self, photos: List[Photo]):
        self.__photos = photos
        for photo in photos:
            self.__layout.addWidget(PhotoListViewItem(photo, self.__openPhoto))

    def __openPhoto(self):
        window = self.window()
        photoViewerPanel = window.getPhotoViewerPanel()
        photoViewerPanel.setPhoto(self.sender().property('photo'))
        window.setActivePanel(photoViewerPanel)

class PhotoListViewItem(QPushButton):
    def __init__(self, photo: Photo, clickSlot: Callable, parent: QWidget = None):
        super(PhotoListViewItem, self).__init__(parent)

        self.setProperty('photo', photo)
        pixmap = QPixmap(photo.path)
        fixedHeight = 320
        fullWidgetSize = QSize(pixmap.width() / pixmap.height() * fixedHeight, fixedHeight)

        self.setMaximumSize(fullWidgetSize)
        self.setMinimumSize(QSize(fullWidgetSize.width() / 2, fixedHeight))

        self.setFlat(True)
        self.setIcon(QIcon(pixmap.scaled(fullWidgetSize, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)))
        self.setIconSize(fullWidgetSize)
        self.clicked.connect(clickSlot)
