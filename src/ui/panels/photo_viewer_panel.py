"""
...
"""

import os
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from ui.generated.photo_viewer_panel_ui import Ui_PhotoViewerPanel
from ui.widgets.aspect_ratio_image import AspectRatioImage
from ui.dependencies import *

class PhotoViewerPanel(QWidget):
    def __init__(self, parent=None):
        super(PhotoViewerPanel, self).__init__(parent)

        self.ui = Ui_PhotoViewerPanel()
        self.ui.setupUi(self)

    def set_photo(self, photo: Photo):
        pixmap = QPixmap(photo.path)
        self.ui.photo.setPixmap(pixmap)
        self.ui.photo.setObjectDetectionBoxes([], [])
        self.ui.name_value_label.setText(os.path.basename(photo.path))
        self.ui.size_value_label.setText(str(round(os.path.getsize(photo.path) / 1000, 1)) + ' KB')
        self.ui.dimensions_value_label.setText(str(pixmap.width()) + 'x' + str(pixmap.height()))
        self.ui.date_value_label.setText('Inconnue' if photo.date is None else photo.date.strftime("%d/%m/%Y"))
        self.ui.place_value_label.setText('Inconnu' if photo.place is None else photo.place)

        self.clear_layout(self.ui.classifications)
        if (len(photo.classifications) == 0):
            self.ui.classifications.addWidget(QLabel('Aucune classification'))
        for classification in photo.classifications:
            self.ui.classifications.addWidget(QLabel(classification))

    def clear_layout(self, layout):
        for i in reversed(range(layout.count())):
            layout.itemAt(i).widget().setParent(None)

    @pyqtSlot(name='on_back_button_clicked')
    def return_to_photo_gallery(self):
        self.window().set_panel(self.window().photo_gallery_panel)
