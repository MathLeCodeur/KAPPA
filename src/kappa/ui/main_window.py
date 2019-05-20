from PyQt5.QtWidgets import QMainWindow

from kappa.controllers.FaceVectorController import FaceVectorController
from kappa.controllers.ImageController import ImageController
from kappa.controllers.ObjectVectorController import ObjectVectorController
from kappa.ui.generated.main_window_ui import Ui_MainWindow
from kappa.ui.panels.photo_gallery_panel import PhotoGalleryPanel
from kappa.ui.panels.photo_viewer_panel import PhotoViewerPanel

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.__ui = Ui_MainWindow()
        self.__ui.setupUi(self)

        self.faceVectorController = FaceVectorController()
        self.imageController = ImageController()
        self.objectVectorController = ObjectVectorController()

        self.__createWidgets()


    def __createWidgets(self):
        self.__photoGalleryPanel = PhotoGalleryPanel()
        self.__photoViewerPanel = PhotoViewerPanel()

        self.__photoGalleryPanel.setPhotos(self.imageController.getAll())

        self.__ui.stackedWidget.addWidget(self.__photoGalleryPanel)
        self.__ui.stackedWidget.addWidget(self.__photoViewerPanel)

    def getPhotoGalleryPanel(self) -> PhotoGalleryPanel:
        return self.__photoGalleryPanel

    def getPhotoViewerPanel(self) -> PhotoViewerPanel:
        return self.__photoViewerPanel

    def setActivePanel(self, panel):
        self.__ui.stackedWidget.setCurrentWidget(panel)

    def reload(self):
        self.hide()
        self.__ui.stackedWidget.removeWidget(self.__photoGalleryPanel)
        self.__ui.stackedWidget.removeWidget(self.__photoViewerPanel)
        self.__createWidgets()
        self.show()
