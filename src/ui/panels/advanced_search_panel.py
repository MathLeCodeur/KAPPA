"""
Panel de recherche avancée dans la gallerie photo.
"""

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from ui.generated.advanced_search_panel_ui import *
from ui.generated.advanced_search_sub_panel_ui import *

class AdvancedSearchPanel(QWidget):
    def __init__(self, parent: QWidget = None):
        super(AdvancedSearchPanel, self).__init__(parent)

        self.__ui = Ui_AdvancedSearchPanel()
        self.__ui.setupUi(self)

        self.__ui.searchConditionsContainerLayout.addWidget(AdvancedSearchSubPanel())

        self.__conditionCount = 1
        self.__maxConditionCount = 4

    @pyqtSlot(name='on_addSmallActionButton_clicked')
    def addAdvancedSearchPSubanel(self):
        if self.__conditionCount < self.__maxConditionCount:
            self.__ui.searchConditionsContainerLayout.addWidget(AdvancedSearchSubPanel())
            self.__conditionCount += 1

    @pyqtSlot(name='on_removeSmallActionButton_clicked')
    def removeAdvancedSearchSubPanel(self):
        if self.__conditionCount > 1:
            widget = self.__ui.searchConditionsContainerLayout.itemAt(self.__conditionCount - 1).widget()
            self.__ui.searchConditionsContainerLayout.removeWidget(widget)
            widget.deleteLater()
            self.__conditionCount -= 1

class AdvancedSearchSubPanel(QWidget):
    def __init__(self, parent: QWidget = None):
        super(AdvancedSearchSubPanel, self).__init__(parent)

        self.__ui = Ui_AdvancedSearchSubPanel()
        self.__ui.setupUi(self)

        self.updateOperatorComboBox(self.__ui.fieldComboBox.currentText())

    @pyqtSlot(str, name='on_fieldComboBox_currentIndexChanged')
    def updateOperatorComboBox(self, label: str):
        self.__ui.operatorComboBox.clear()

        if label == 'Date':
            self.__ui.operatorComboBox.addItem('égale à')
            self.__ui.operatorComboBox.addItem('supérieure à')
            self.__ui.operatorComboBox.addItem('inférieure à')
            self.__ui.operatorComboBox.addItem('entre')

            self.__ui.operand1LineEdit.setInputMethodHints(Qt.ImhDate)
        else:
            self.__ui.operatorComboBox.addItem('contient')

            self.__ui.operand1LineEdit.setInputMethodHints(Qt.ImhNone)

    @pyqtSlot(str, name='on_operatorComboBox_currentIndexChanged')
    def updateOperand2Visibility(self, label: str):
        visibility = label == 'entre'

        self.__ui.andLabel.setVisible(visibility)
        self.__ui.operand2LineEdit.setVisible(visibility)
