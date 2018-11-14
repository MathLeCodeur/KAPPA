"""
Widget permettant d'afficher une liste de photos.
"""

import random
from typing import List
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from ui.dependencies import Photo

class PhotoListView(QWidget):
    def __init__(self, parent=None):
        super(PhotoListView, self).__init__(parent)

        self.photo_size = QSize(256, 256)
        self.photo_count_per_row = 0

        self.layout = QVBoxLayout()
        self.layout.setAlignment(Qt.AlignTop)
        self.layout.setSpacing(0)
        self.setLayout(self.layout)

    def set_photos(self, photos: List[Photo]):
        self.photos = photos
        self.update_photo_count_per_row()
        self.refresh()

    def update_photo_count_per_row(self):
        self.photo_count_per_row = max(2, self.width() // (self.photo_size.width() + 25))

    def refresh(self):
        self.clear_layout(self.layout)

        i = 0
        photo_count = len(self.photos)

        while i < photo_count:
            self.layout.addWidget(self.create_photo_row(self.photos[i:i+self.photo_count_per_row]))
            i += self.photo_count_per_row

    def clear_layout(self, layout):
        for i in reversed(range(layout.count())):
            layout.itemAt(i).widget().setParent(None)

    def create_photo_row(self, photos: List[Photo]):
        row = QWidget()
        row_layout = QHBoxLayout()
        row_layout.setAlignment(Qt.AlignLeft)
        row_layout.setSpacing(5)

        for photo in photos:
            photo_button = QPushButton()
            photo_button.setFlat(True)
            photo_button.setIcon(QIcon(QPixmap(photo.path).scaled(self.photo_size)))
            photo_button.setIconSize(self.photo_size)
            photo_button.setProperty('photo', photo)
            photo_button.clicked.connect(self.open_photo)
            row_layout.addWidget(photo_button)

        row.setLayout(row_layout)
        return row

    def resizeEvent(self, resizeEvent: QResizeEvent):
        old_photo_count_per_row = self.photo_count_per_row
        self.update_photo_count_per_row()

        if self.photo_count_per_row != old_photo_count_per_row:
            self.refresh()

    def open_photo(self):
        window = self.window()
        photo_viewer_panel = window.photo_viewer_panel
        photo_viewer_panel.set_photo(self.sender().property('photo'))
        window.set_panel(photo_viewer_panel)
