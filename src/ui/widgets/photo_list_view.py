"""
Widget permettant d'afficher une liste de photos.
"""

from typing import List
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

    def set_photos(self, photos: List[Photo]):
        self.photos = photos
        for photo in photos:
            self.layout.addWidget(PhotoListViewItem(photo, self.open_photo))

    def open_photo(self):
        window = self.window()
        photo_viewer_panel = window.photo_viewer_panel
        photo_viewer_panel.set_photo(self.sender().property('photo'))
        window.set_panel(photo_viewer_panel)

class PhotoListViewItem(QPushButton):
    def __init__(self, photo: Photo, clicked_slot, parent=None):
        super(PhotoListViewItem, self).__init__(parent)

        self.setProperty('photo', photo)
        self.pixmap = QPixmap(photo.path)
        self.fixed_height = 320
        full_widget_size = QSize(self.pixmap.width() / self.pixmap.height() * self.fixed_height, self.fixed_height)

        self.setMaximumSize(full_widget_size)
        self.setMinimumSize(QSize(full_widget_size.width() / 2, self.fixed_height))

        self.setFlat(True)
        self.setIcon(QIcon(self.pixmap.scaled(full_widget_size, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)))
        self.setIconSize(full_widget_size)
        self.clicked.connect(clicked_slot)
