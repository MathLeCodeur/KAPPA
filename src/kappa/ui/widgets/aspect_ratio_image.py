"""
Widget permettant d'afficher une image de taille dynamique en conservant son aspect ratio.
"""

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class AspectRatioImage(QLabel):
    clicked = pyqtSignal()

    def __init__(self, pixmap: QPixmap = None, parent: QWidget = None):
        super(AspectRatioImage, self).__init__(parent)

        self.__pixmap = None
        self.__scaledPixmap = None

        self.setPixmap(pixmap)
        self.setMinimumSize(1, 1)
        self.setScaledContents(False)
        self.setAlignment(Qt.AlignCenter)
        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)

    def setPixmap(self, pixmap: QPixmap):
        if pixmap:
            self.__pixmap = pixmap
            super().setPixmap(self.__getScaledPixmap())

    def heightForWidth(self, width: int) -> int:
        return self.height() if self.__pixmap is None else (self.__pixmap.height() * width) / self.__pixmap.width()

    def sizeHint(self) -> QSize:
        if self.__scaledPixmap:
            return self.__scaledPixmap.size()
        return QSize()

    def resizeEvent(self, resizeEvent: QResizeEvent):
        if self.__pixmap != None:
            super().setPixmap(self.__getScaledPixmap())

    def __getScaledPixmap(self) -> QPixmap:
        self.__scaledPixmap = self.__pixmap.scaled(self.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        return self.__scaledPixmap
