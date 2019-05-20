"""
Panel de recherche avancée dans la gallerie photo.
"""

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from kappa.ui.generated.advanced_search_panel_ui import *
from kappa.ui.generated.advanced_search_sub_panel_ui import *
from kappa.interoperability.image_query import *

class AdvancedSearchPanel(QDialog):
    def __init__(self, parent: QWidget = None):
        super(AdvancedSearchPanel, self).__init__(parent)

        self.__ui = Ui_AdvancedSearchPanel()
        self.__ui.setupUi(self)

        self.__maxConditionCount = 4

        self.__imageQuery = None

    def getImageQuery(self) -> ImageQuery:
        return self.__imageQuery

    def setImageQuery(self, imageQuery: ImageQuery):
        conditions = imageQuery.getConditions()

        for i in range(self.__ui.searchConditionsContainerLayout.count()):
            self.removeAdvancedSearchSubPanel()
        self.addAdvancedSearchSubpanel()

        for i in range(min(len(conditions), self.__maxConditionCount)):
            if i > 0:
                self.addAdvancedSearchSubpanel()
            advancedSearchSubPanel = self.__ui.searchConditionsContainerLayout.itemAt(i).widget()
            advancedSearchSubPanel.setCondition(conditions[i])

    def updateButtons(self):
        if self.__ui.searchConditionsContainerLayout.count() <= 1:
            self.__ui.removeSmallActionButton.setEnabled(False)
        else:
            self.__ui.removeSmallActionButton.setEnabled(True)

        if self.__ui.searchConditionsContainerLayout.count() == self.__maxConditionCount:
            self.__ui.addSmallActionButton.setEnabled(False)
        else:
            self.__ui.addSmallActionButton.setEnabled(True)

    @pyqtSlot(name='on_addSmallActionButton_clicked')
    def addAdvancedSearchSubpanel(self):
        if self.__ui.searchConditionsContainerLayout.count() < self.__maxConditionCount:
            self.__ui.searchConditionsContainerLayout.addWidget(AdvancedSearchSubPanel())
            self.updateButtons()

    @pyqtSlot(name='on_removeSmallActionButton_clicked')
    def removeAdvancedSearchSubPanel(self):
        if self.__ui.searchConditionsContainerLayout.count() > 0:
            widget = self.__ui.searchConditionsContainerLayout.itemAt(self.__ui.searchConditionsContainerLayout.count() - 1).widget()
            self.__ui.searchConditionsContainerLayout.removeWidget(widget)
            widget.deleteLater()
            self.updateButtons()

    @pyqtSlot(name='on_okButton_clicked')
    def acceptImageSearch(self):
        self.__imageQuery = None
        imageQuery = ImageQuery()

        for i in range(0, self.__ui.searchConditionsContainerLayout.count()):
            advancedSearchSubPanel = self.__ui.searchConditionsContainerLayout.itemAt(i).widget()

            try:
                condition = advancedSearchSubPanel.getCondition()
                imageQuery.addCondition(condition)
            except ImageQueryError as imageQueryError:
                print('error')
                return

        self.__imageQuery = imageQuery
        self.accept()

    @pyqtSlot(name='on_cancelButton_clicked')
    def rejectImageSearch(self):
        self.reject()

class AdvancedSearchSubPanel(QWidget):
    def __init__(self, parent: QWidget = None):
        super(AdvancedSearchSubPanel, self).__init__(parent)

        self.__ui = Ui_AdvancedSearchSubPanel()
        self.__ui.setupUi(self)

        self.updateOperatorComboBox(self.__ui.fieldComboBox.currentText())

    def getCondition(self) -> ImageQueryCondition:
        return ImageQueryCondition(
            ImageQueryField(self.__ui.fieldComboBox.currentIndex()),
            ImageQueryOperator(self.__ui.operatorComboBox.currentIndex() if self.__ui.operatorComboBox.currentText() != 'contient' else 4),
            self.__ui.operand1LineEdit.text(), self.__ui.operand2LineEdit.text())

    def setCondition(self, imageQueryCondition: ImageQueryCondition):
        self.__ui.fieldComboBox.setCurrentIndex(imageQueryCondition.getField().value)
        self.__ui.operatorComboBox.setCurrentIndex(imageQueryCondition.getOperator().value % 4)
        self.__ui.operand1LineEdit.setText(imageQueryCondition.getOperand1())
        self.__ui.operand2LineEdit.setText(imageQueryCondition.getOperand2())

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
