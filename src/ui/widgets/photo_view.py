"""
Widget permettant d'afficher une photo avec les boîtes englobantes des objetsdétectés.
"""

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from ui.widgets.aspect_ratio_image import AspectRatioImage

class PhotoView(AspectRatioImage):
    def __init__(self, parent: QWidget = None):
        super(PhotoView, self).__init__(parent)

        self.rectangles = []
        self.names = []

    def setObjectDetectionBoxes(self, rectangles, names):
        self.rectangles = rectangles
        self.names = names

    def paintEvent(self, event):
        super().paintEvent(event)
        painter = QPainter(self)
        pen = QPen(Qt.red)
        pen.setWidth(5)
        painter.setPen(pen)

        height = self.pixmap().height()
        width = self.pixmap().width()

        x_offset = self.height() / 2 - height / 2
        y_offset = self.height() / 2 - height / 2

        painter.drawRect(QRect(100, 100 + y_offset, 100, 100))

        for i in range(0, len(self.rectangles)):
            painter.drawRect(QRect(100, 100, 100, 100))
