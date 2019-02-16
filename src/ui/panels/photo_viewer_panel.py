"""
Affichage d'une seule photo avec ses métadonnées associées.
"""

import os

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from face_detection.inference_image_face import *
from ui.dependencies import *
from ui.generated.photo_viewer_panel_ui import *
from ui.widgets.aspect_ratio_image import *

class PhotoViewerPanel(QWidget):
    def __init__(self, parent=None):
        super(PhotoViewerPanel, self).__init__(parent)

        self.ui = Ui_PhotoViewerPanel()
        self.ui.setupUi(self)
        self.faceDetector = TensoflowFaceDector()

    def setPhoto(self, photo: Photo):
        pixmap = QPixmap(photo.path)
        self.ui.photo.setPixmap(pixmap)
        self.ui.photo.setDetectionBoxes(self.faceDetector.getBoxes(photo.path))
        self.ui.name.setText(os.path.basename(photo.path))
        self.ui.size.setText(str(round(os.path.getsize(photo.path) / 1000, 1)) + ' KB')
        self.ui.dimensions.setText(str(pixmap.width()) + 'x' + str(pixmap.height()))
        self.ui.date.setText('Inconnue' if photo.date is None else photo.date.strftime("%d/%m/%Y"))
        self.ui.place.setText('Inconnu' if photo.place is None else photo.place)

        self.clear_layout(self.ui.classifications)
        if (len(photo.classifications) == 0):
            self.ui.classifications.addWidget(QLabel('Aucune classification'))
        for classification in photo.classifications:
            self.ui.classifications.addWidget(QLabel(classification))

    def clear_layout(self, layout):
        for i in reversed(range(layout.count())):
            layout.itemAt(i).widget().setParent(None)

    @pyqtSlot(name='on_backButton_clicked')
    def return_to_photo_gallery(self):
        self.window().setActivePanel(self.window().photoGalleryPanel)
