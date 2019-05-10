from PyQt5.QtGui import QIcon
from PyQt5.QtDesigner import QPyDesignerCustomWidgetPlugin
from kappa.ui.widgets.photo_list_view import PhotoListView

class PhotoListViewWidget(QPyDesignerCustomWidgetPlugin):
    def __init__(self, parent=None):
        super(PhotoListViewWidget, self).__init__(parent)
        self.__initialized = False

    def initialize(self, core):
        if self.__initialized:
            return
        self.__initialized = True

    def isInitialized(self):
        return self.__initialized

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
        return "kappa.ui.widgets.photo_list_view"
