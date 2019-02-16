"""
Widget permettant d'afficher une image de taille dynamique en conservant son aspect ratio.
"""

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class AspectRatioImage(QLabel):
    def __init__(self, pixmap: QPixmap = None, parent: QWidget = None):
        super(AspectRatioImage, self).__init__(parent)

        self.setPixmap(pixmap)
        self.setMinimumSize(1, 1)
        self.setScaledContents(False)
        self.setAlignment(Qt.AlignCenter)

    def setPixmap(self, pixmap: QPixmap):
        self._pixmap = pixmap
        if pixmap:
            super().setPixmap(self._get_scaled_pixmap())

    def heightForWidth(self, width: int):
        return self.height() if self._pixmap is None else (self._pixmap.height() * width) / self._pixmap.width()

    def sizeHint(self):
        width = self.width()
        return QSize(width, self.heightForWidth(width))

    def resizeEvent(self, resizeEvent: QResizeEvent):
        if self._pixmap != None:
            super().setPixmap(self._get_scaled_pixmap())

    def _get_scaled_pixmap(self):
        return self._pixmap.scaled(self.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
