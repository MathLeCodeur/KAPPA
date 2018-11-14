from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot
from ui.generated.main_window_ui import Ui_MainWindow
from ui.panels.photo_gallery_panel import PhotoGalleryPanel
from ui.panels.photo_viewer_panel import PhotoViewerPanel

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.photo_gallery_panel = PhotoGalleryPanel()
        self.photo_viewer_panel = PhotoViewerPanel()

        self.ui.stacked_widget.addWidget(self.photo_gallery_panel)
        self.ui.stacked_widget.addWidget(self.photo_viewer_panel)

    def set_panel(self, panel: QWidget):
        self.ui.stacked_widget.setCurrentWidget(panel)
