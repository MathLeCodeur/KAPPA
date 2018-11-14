"""
...
"""

from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSlot
from ui.generated.photo_gallery_panel_ui import Ui_PhotoGalleryPanel
from ui.dependencies import *

class PhotoGalleryPanel(QWidget):
    def __init__(self, parent=None):
        super(PhotoGalleryPanel, self).__init__(parent)

        self.ui = Ui_PhotoGalleryPanel()
        self.ui.setupUi(self)

        self.photos = get_photos('date', 'desc')
        self.ui.photo_list_view.set_photos(self.photos)

    @pyqtSlot(name='on_search_button_clicked')
    def search_photos_by_file_name(self):
        pass

    @pyqtSlot(name='on_advanced_search_button_clicked')
    def toggle_advanced_search(self):
        pass

    @pyqtSlot(name='on_sorting_button_clicked')
    def sort_photos(self):
        pass
