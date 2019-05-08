import sys

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class FlowLayout(QLayout):
    def __init__(self, parent=None, margin=-1, hspacing=-1, vspacing=-1):
        super(FlowLayout, self).__init__(parent)
        self.__hspacing = hspacing
        self.__vspacing = vspacing
        self.__items = []
        self.setContentsMargins(margin, margin, margin, margin)

    def __del__(self):
        del self.__items[:]

    def addItem(self, item):
        self.__items.append(item)

    def horizontalSpacing(self):
        if self.__hspacing >= 0:
            return self.__hspacing
        else:
            return self.smartSpacing(QStyle.PM_LayoutHorizontalSpacing)

    def verticalSpacing(self):
        if self.__vspacing >= 0:
            return self.__vspacing
        else:
            return self.smartSpacing(QStyle.PM_LayoutVerticalSpacing)

    def count(self):
        return len(self.__items)

    def itemAt(self, index):
        if 0 <= index < len(self.__items):
            return self.__items[index]

    def takeAt(self, index):
        if 0 <= index < len(self.__items):
            return self.__items.pop(index)

    def expandingDirections(self):
        return Qt.Orientations(0)

    def hasHeightForWidth(self):
        return True

    def heightForWidth(self, width):
        return self.doLayout(QRect(0, 0, width, 0), True)

    def setGeometry(self, rect):
        super(FlowLayout, self).setGeometry(rect)
        self.doLayout(rect, False)

    def sizeHint(self):
        return self.minimumSize()

    def minimumSize(self):
        size = QSize()
        for item in self.__items:
            size = size.expandedTo(item.minimumSize())
        left, top, right, bottom = self.getContentsMargins()
        size += QSize(left + right, top + bottom)
        return size

    def doLayout(self, rect, testonly):
        left, top, right, bottom = self.getContentsMargins()
        effective = rect.adjusted(+left, +top, -right, -bottom)

        x = effective.x()
        y = effective.y()
        lineheight = 0
        row_width_ratio = self.getRowWidthRatio(rect, 0)
        isFirst = 0

        for i in range(self.count()):
            item = self.__items[i]
            widget = item.widget()
            hspace = self.horizontalSpacing()
            if hspace == -1:
                hspace = widget.style().layoutSpacing(
                    QSizePolicy.PushButton,
                    QSizePolicy.PushButton, Qt.Horizontal)
            vspace = self.verticalSpacing()
            if vspace == -1:
                vspace = widget.style().layoutSpacing(
                    QSizePolicy.PushButton,
                    QSizePolicy.PushButton, Qt.Vertical)

            nextX = int(x + item.maximumSize().width() * row_width_ratio + hspace)
            if nextX - hspace > effective.right():
                x = effective.x()
                y = y + lineheight + vspace
                row_width_ratio = self.getRowWidthRatio(rect, i)
                nextX = int(x + item.maximumSize().width() * row_width_ratio + hspace)
                lineheight = 0
            if not testonly:
                item.setGeometry(
                    QRect(QPoint(x, y), QSize(item.maximumSize().width() * row_width_ratio, item.sizeHint().height())))
            x = nextX
            lineheight = max(lineheight, item.sizeHint().height())
        return y + lineheight - rect.y() + bottom

    def getRowWidthRatio(self, rect, i):
        left, top, right, bottom = self.getContentsMargins()
        effective = rect.adjusted(+left, +top, -right, -bottom)
        total_horizontal_spacing = 0
        maximum_line_width = 0

        for j in range(i, self.count()):
            item = self.__items[j]

            if i == j:
                hspace = 0
            else:
                hspace = self.horizontalSpacing()
                if hspace == -1:
                    hspace = item.widget().style().layoutSpacing(
                        QSizePolicy.PushButton,
                        QSizePolicy.PushButton, Qt.Horizontal)

            if maximum_line_width + total_horizontal_spacing > effective.width():
                break
            maximum_line_width += item.maximumSize().width()
            total_horizontal_spacing += hspace
        if maximum_line_width > 0:
            return min((effective.width() - (j-i-1) * hspace) / maximum_line_width, 1)
        return 0.5

    def smartSpacing(self, pm):
        parent = self.parent()
        if parent is None:
            return -1
        elif parent.isWidgetType():
            return parent.style().pixelMetric(pm, None, parent)
        else:
            return parent.spacing()
