"""
Widget permettant d'afficher une photo avec les boîtes englobantes des objets détectés.
"""

import os
import tempfile
from typing import *

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import config
import context

class PhotoView(QGraphicsView):
    def __init__(self, parent: QWidget = None):
        super(PhotoView, self).__init__(parent=parent)

        self.__scene = QGraphicsScene()
        self.setScene(self.__scene)

        self.__pixmapItem = self.__scene.addPixmap(QPixmap())

        self.__sceneWidgets = []
        self.__tagData = []

        self.setAlignment(Qt.AlignCenter)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setStyleSheet("background: transparent; border: none;")

    def pixmap(self):
        return self.__pixmapItem.pixmap()

    def setPixmap(self, pixmap: QPixmap):
        if pixmap:
            self.__pixmapItem.setPixmap(pixmap)
            self.resizeEvent(None)

    def setRecognizedPeopleAndObjects(self, recognizedPeopleAndObjects: Dict[str, List[List[int]]]):
        self.__tagData = recognizedPeopleAndObjects

        for sceneWidget in self.__sceneWidgets:
            self.scene().removeItem(sceneWidget)
        self.__sceneWidgets.clear()

        pen = QPen(QColor(config.get('themeColor')), 5)
        pen.setJoinStyle(Qt.MiterJoin)
        pen.setCosmetic(True)

        font = QFont(config.get('themeFont'), 11, 100)
        fontMetrics = QFontMetrics(font)

        imageWidth, imageHeight = self.pixmap().width(), self.pixmap().height()

        for tagData_ in self.__tagData:
            box, name = tagData_['boundingBox'], tagData_['name']
            yMin = box[0]
            xMax = box[1]
            yMax = box[2]
            xMin = box[3]

            boxWidth, boxHeight = xMax - xMin, yMax - yMin
            boxCenterX, boxCenterY = xMin + boxWidth / 2, yMin + boxHeight / 2
            lineEditWidth, lineEditHeight = self.mapToScene(self.width(), 0).x() / 5, imageHeight / 20

            lineEdit = QLineEdit(name)

            # Write to __tagData
            tagData_['lineEdit'] = lineEdit

            lineEditItem = self.scene().addWidget(lineEdit)

            lineEditFont = lineEditItem.widget().font()
            lineEditFont.setPixelSize(lineEditWidth / 12)
            lineEditItem.widget().setFont(lineEditFont)
            lineEditItem.widget().setAlignment(Qt.AlignCenter)
            lineEdit.setTextMargins(0, 0, 0, 0)
            lineEditItem.widget().setTextMargins(0, 0, 0, 0)

            lineEditItem.setGeometry(QRectF(boxCenterX - lineEditWidth / 2, yMax + lineEditHeight / 2, lineEditWidth, lineEditHeight))

            self.__sceneWidgets.append(lineEditItem)
            self.__sceneWidgets.append(self.scene().addRect(QRectF(xMin, yMin, boxWidth, boxHeight), pen))

    def resizeEvent(self, event: QResizeEvent):
        self.setSceneRect(0, 0, self.pixmap().width(), self.pixmap().height())
        self.fitInView(self.__pixmapItem, Qt.KeepAspectRatio)
        super().resizeEvent(event)

    def saveTagData(self, photoPath: str):
        for tagData_ in self.__tagData:
            self.window().faceVectorController.commitFaceVectorChange(tagData_['name'], tagData_['lineEdit'].text(), photoPath, tagData_['boundingBox'], tagData_['vector'])
