from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from ui.generated.photo_gallery_panel_ui import *
from ui.dependencies import *

class PhotoGalleryPanel(QWidget):
    def __init__(self, parent=None):
        super(PhotoGalleryPanel, self).__init__(parent)

        self.ui = Ui_PhotoGalleryPanel()
        self.ui.setupUi(self)

        self.photos = getPhotos('date', 'desc')
        self.ui.photoListView.setPhotos(self.photos)

    @pyqtSlot(name='on_searchButton_clicked')
    def search_photos_by_file_name(self):
        pass

    @pyqtSlot(name='on_advancedSearchButton_clicked')
    def toggle_advanced_search(self):
        pass

    @pyqtSlot(name='on_sortingButton_clicked')
    def sort_photos(self):
        pass
