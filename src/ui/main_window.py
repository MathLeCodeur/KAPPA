from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from ui.generated.main_window_ui import *
from ui.panels.photo_gallery_panel import *
from ui.panels.photo_viewer_panel import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.photoGalleryPanel = PhotoGalleryPanel()
        self.photoViewerPanel = PhotoViewerPanel()

        self.ui.stackedWidget.addWidget(self.photoGalleryPanel)
        self.ui.stackedWidget.addWidget(self.photoViewerPanel)

    def setActivePanel(self, panel: QWidget):
        self.ui.stackedWidget.setCurrentWidget(panel)
