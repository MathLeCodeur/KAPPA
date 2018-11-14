from PyQt5.QtGui import QIcon
from PyQt5.QtDesigner import QPyDesignerCustomWidgetPlugin
from ui.widgets.photo_list_view import PhotoListView

class PhotoListViewWidget(QPyDesignerCustomWidgetPlugin):
    def __init__(self, parent=None):
        super(PhotoListViewWidget, self).__init__(parent)
        self.initialized = False

    def initialize(self, core):
        if self.initialized:
            return
        self.initialized = True

    def isInitialized(self):
        return self.initialized

    def createWidget(self, parent):
        return PhotoListView(parent)

    def name(self):
        return "PhotoListView"

    def group(self):
        return "KAPPA Widgets"

    def icon(self):
        return QIcon()

    def toolTip(self):
        return ""

    def whatsThis(self):
        return ""

    def isContainer(self):
        return False

    def includeFile(self):
        return "ui.widgets.photo_list_view"
