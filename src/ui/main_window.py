from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from ui.generated.main_window_ui import *
from ui.panels.photo_gallery_panel import *
from ui.panels.photo_viewer_panel import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.__ui = Ui_MainWindow()
        self.__ui.setupUi(self)

        self.__createWidgets()

    def __createWidgets(self):
        self.__photoGalleryPanel = PhotoGalleryPanel()
        self.__photoViewerPanel = PhotoViewerPanel()

        self.__ui.stackedWidget.addWidget(self.__photoGalleryPanel)
        self.__ui.stackedWidget.addWidget(self.__photoViewerPanel)

    def getPhotoGalleryPanel(self) -> PhotoGalleryPanel:
        return self.__photoGalleryPanel

    def getPhotoViewerPanel(self) -> PhotoViewerPanel:
        return self.__photoViewerPanel

    def setActivePanel(self, panel: QWidget):
        self.__ui.stackedWidget.setCurrentWidget(panel)

    def reload(self):
        self.hide()
        self.__ui.stackedWidget.removeWidget(self.__photoGalleryPanel)
        self.__ui.stackedWidget.removeWidget(self.__photoViewerPanel)
        self.__createWidgets()
        self.show()
