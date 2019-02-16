"""
Widget permettant d'afficher une liste de photos.
"""

from typing import *

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from ui.widgets.flow_layout import *
from ui.dependencies import *

class PhotoListView(QWidget):
    def __init__(self, parent=None):
        super(PhotoListView, self).__init__(parent)

        self.layout = FlowLayout(self, 30, 16, 16)
        self.setLayout(self.layout)

    def setPhotos(self, photos: List[Photo]):
        self.photos = photos
        for photo in photos:
            self.layout.addWidget(PhotoListViewItem(photo, self.openPhoto))

    def openPhoto(self):
        window = self.window()
        photoViewerPanel = window.photoViewerPanel
        photoViewerPanel.setPhoto(self.sender().property('photo'))
        window.setActivePanel(photoViewerPanel)

class PhotoListViewItem(QPushButton):
    def __init__(self, photo: Photo, clicked_slot, parent=None):
        super(PhotoListViewItem, self).__init__(parent)

        self.setProperty('photo', photo)
        self.pixmap = QPixmap(photo.path)
        self.fixed_height = 320
        fullWidgetSize = QSize(self.pixmap.width() / self.pixmap.height() * self.fixed_height, self.fixed_height)

        self.setMaximumSize(fullWidgetSize)
        self.setMinimumSize(QSize(fullWidgetSize.width() / 2, self.fixed_height))

        self.setFlat(True)
        self.setIcon(QIcon(self.pixmap.scaled(fullWidgetSize, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)))
        self.setIconSize(fullWidgetSize)
        self.clicked.connect(clicked_slot)
