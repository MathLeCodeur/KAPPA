"""
Affichage de toutes les photos de l'utilisateur, avec la possibilité de les trier et d'effectuer une
recherche filtrant les photos affichées.
"""

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from ui.dependencies import *
from ui.generated.photo_gallery_panel_ui import *

class PhotoGalleryPanel(QWidget):
    def __init__(self, parent: QWidget = None):
        super(PhotoGalleryPanel, self).__init__(parent)

        self.__ui = Ui_PhotoGalleryPanel()
        self.__ui.setupUi(self)

        self.__photos = getPhotos('date', 'desc')
        self.__ui.photoListView.setPhotos(self.__photos)

    @pyqtSlot(name='on_searchButton_clicked')
    def searchPhotosByFileName(self):
        pass

    @pyqtSlot(name='on_advancedSearchButton_clicked')
    def toggleAdvancedSearchPanel(self):
        pass

    @pyqtSlot(name='on_sortingButton_clicked')
    def sortPhotos(self):
        pass
