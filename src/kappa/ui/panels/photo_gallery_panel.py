"""
Affichage de toutes les photos de l'utilisateur, avec la possibilité de les trier et d'effectuer une
recherche filtrant les photos affichées.
"""

from pathlib import Path

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

import config
from kappa.models.ImageModel import *
from kappa.ui.generated.photo_gallery_panel_ui import *
from kappa.ui.panels.advanced_search_panel import *

class PhotoGalleryPanel(QWidget):
    def __init__(self, parent: QWidget = None):
        super(PhotoGalleryPanel, self).__init__(parent)

        self.__ui = Ui_PhotoGalleryPanel()
        self.__ui.setupUi(self)

        self.__photos = []

        self.__advancedSearchPanel = AdvancedSearchPanel(self)
        self.__imageQuery = ImageQuery()

    def setPhotos(self, photos: ImageModel):
        self.__photos = photos
        self.__ui.photoListView.setPhotos(self.__photos)

    @pyqtSlot(name='on_searchLineEdit_returnPressed')
    def updateImageQuery(self):
        try:
            self.__imageQuery = ImageQuery.fromImageQueryLanguage(self.__ui.searchLineEdit.text())
        except ImageQueryError as imageQueryError:
            print('error')

    @pyqtSlot(name='on_advancedSearchActionButton_clicked')
    def openAdvancedSearchPanel(self):
        self.__advancedSearchPanel.setImageQuery(self.__imageQuery)

        if self.__advancedSearchPanel.exec() == QDialog.Accepted:
            self.__imageQuery = self.__advancedSearchPanel.getImageQuery()
            self.__ui.searchLineEdit.setText(self.__imageQuery.toImageQueryLanguage())

    @pyqtSlot(name='on_importFolderActionButton_clicked')
    def importFolder(self):
        directory = QFileDialog.getExistingDirectory(
            self, 'Importer un répertoire d\'images',
            str(Path.home()),
            QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks
        )

        if directory:
            self.window().imageController.importImageFolder(directory)
            self.setPhotos(self.window().imageController.getAll())

    @pyqtSlot(name='on_changeThemeActionButton_clicked')
    def changeTheme(self):
        if (config.get('theme') == 'dark'):
            config.set('theme', 'light')
            config.set('iconTheme', 'black')
        else:
            config.set('theme', 'dark')
            config.set('iconTheme', 'blue')

        config.loadThemes(qApp, True)
        self.window().reload()
