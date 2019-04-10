import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class FlowLayout(QtWidgets.QLayout):
    def __init__(self, parent=None, margin=-1, hspacing=-1, vspacing=-1):
        super(FlowLayout, self).__init__(parent)
        self._hspacing = hspacing
        self._vspacing = vspacing
        self._items = []
        self.setContentsMargins(margin, margin, margin, margin)

    def __del__(self):
        del self._items[:]

    def addItem(self, item):
        self._items.append(item)

    def horizontalSpacing(self):
        if self._hspacing >= 0:
            return self._hspacing
        else:
            return self.smartSpacing(
                QtWidgets.QStyle.PM_LayoutHorizontalSpacing)

    def verticalSpacing(self):
        if self._vspacing >= 0:
            return self._vspacing
        else:
            return self.smartSpacing(
                QtWidgets.QStyle.PM_LayoutVerticalSpacing)

    def count(self):
        return len(self._items)

    def itemAt(self, index):
        if 0 <= index < len(self._items):
            return self._items[index]

    def takeAt(self, index):
        if 0 <= index < len(self._items):
            return self._items.pop(index)

    def expandingDirections(self):
        return QtCore.Qt.Orientations(0)

    def hasHeightForWidth(self):
        return True

    def heightForWidth(self, width):
        return self.doLayout(QtCore.QRect(0, 0, width, 0), True)

    def setGeometry(self, rect):
        super(FlowLayout, self).setGeometry(rect)
        self.doLayout(rect, False)

    def sizeHint(self):
        return self.minimumSize()

    def minimumSize(self):
        size = QtCore.QSize()
        for item in self._items:
            size = size.expandedTo(item.minimumSize())
        left, top, right, bottom = self.getContentsMargins()
        size += QtCore.QSize(left + right, top + bottom)
        return size

    def doLayout(self, rect, testonly):
        left, top, right, bottom = self.getContentsMargins()
        effective = rect.adjusted(+left, +top, -right, -bottom)
        x = effective.x()
        y = effective.y()
        lineheight = 0
        row_width_ratio = self.get_row_width_ratio(rect, 0)
        isFirst = 0

        for i in range(self.count()):
            item = self._items[i]
            widget = item.widget()
            hspace = self.horizontalSpacing()
            if hspace == -1:
                hspace = widget.style().layoutSpacing(
                    QtWidgets.QSizePolicy.PushButton,
                    QtWidgets.QSizePolicy.PushButton, QtCore.Qt.Horizontal)
            vspace = self.verticalSpacing()
            if vspace == -1:
                vspace = widget.style().layoutSpacing(
                    QtWidgets.QSizePolicy.PushButton,
                    QtWidgets.QSizePolicy.PushButton, QtCore.Qt.Vertical)

            nextX = int(x + item.maximumSize().width() * row_width_ratio + hspace)
            if nextX - hspace > effective.right():
                x = effective.x()
                y = y + lineheight + vspace
                row_width_ratio = self.get_row_width_ratio(rect, i)
                nextX = int(x + item.maximumSize().width() * row_width_ratio + hspace)
                lineheight = 0
            if not testonly:
                item.setGeometry(
                    QtCore.QRect(QtCore.QPoint(x, y), QtCore.QSize(item.maximumSize().width() * row_width_ratio, item.sizeHint().height())))
            x = nextX
            lineheight = max(lineheight, item.sizeHint().height())
        return y + lineheight - rect.y() + bottom

    def get_row_width_ratio(self, rect, i):
        left, top, right, bottom = self.getContentsMargins()
        effective = rect.adjusted(+left, +top, -right, -bottom)
        minimum_line_width_and_spacing = 0
        maximum_line_width = 0

        for j in range(i, self.count()):
            item = self._items[j]
            widget = item.widget()

            if i == j:
                hspace = 0
            else:
                hspace = self.horizontalSpacing()
                if hspace == -1:
                    hspace = widget.style().layoutSpacing(
                        QtWidgets.QSizePolicy.PushButton,
                        QtWidgets.QSizePolicy.PushButton, QtCore.Qt.Horizontal)

            next_minimum_line_width_and_spacing = minimum_line_width_and_spacing + item.minimumSize().width() + hspace
            if next_minimum_line_width_and_spacing > effective.width():
                break
            minimum_line_width_and_spacing = next_minimum_line_width_and_spacing
            maximum_line_width += item.maximumSize().width()
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
