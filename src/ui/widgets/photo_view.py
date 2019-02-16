"""
Widget permettant d'afficher une photo avec les boîtes englobantes des objets détectés.
"""

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from ui.widgets.aspect_ratio_image import *

class PhotoView(AspectRatioImage):
    def __init__(self, parent: QWidget = None):
        super(PhotoView, self).__init__(parent=parent)

        self.detectionBoxes = []

    def setDetectionBoxes(self, boxes):
        self.detectionBoxes = boxes

    def paintEvent(self, event):
        super().paintEvent(event)

        painter = QPainter(self)

        pen = QPen(Qt.blue)
        pen.setWidth(5)
        painter.setPen(pen)

        height = self.pixmap().height()
        width = self.pixmap().width()

        x_offset = self.width() / 2 - width / 2
        y_offset = self.height() / 2 - height / 2

        for i in range(0, len(self.detectionBoxes)):
            box = self.detectionBoxes[i]
            yMin = box[0] * height + y_offset
            xMin = box[1] * width + x_offset
            yMax = box[2] * height + y_offset
            xMax = box[3] * width + x_offset

            painter.drawRect(QRect(xMin, yMin, xMax - xMin, yMax - yMin))
