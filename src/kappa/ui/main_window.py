from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from kappa.controllers.FaceVectorController import *
from kappa.controllers.ImageController import *
from kappa.controllers.ObjectVectorController import *
from kappa.face_detection.inference_image_face import *
from kappa.ui.generated.main_window_ui import *
from kappa.ui.panels.photo_gallery_panel import *
from kappa.ui.panels.photo_viewer_panel import *

class MainWindow(QMainWindow):
    def __init__(self, faceDetector: TensorflowFaceDetector):
        super(MainWindow, self).__init__()

        self.__ui = Ui_MainWindow()
        self.__ui.setupUi(self)

        self.faceDetector = faceDetector

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

    def setActivePanel(self, panel: QWidget):
        self.__ui.stackedWidget.setCurrentWidget(panel)

    def reload(self):
        self.hide()
        self.__ui.stackedWidget.removeWidget(self.__photoGalleryPanel)
        self.__ui.stackedWidget.removeWidget(self.__photoViewerPanel)
        self.__createWidgets()
        self.show()
