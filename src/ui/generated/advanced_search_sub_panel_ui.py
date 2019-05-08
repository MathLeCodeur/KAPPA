# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'res/ui/advanced_search_sub_panel.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AdvancedSearchSubPanel(object):
    def setupUi(self, AdvancedSearchSubPanel):
        AdvancedSearchSubPanel.setObjectName("AdvancedSearchSubPanel")
        AdvancedSearchSubPanel.resize(405, 49)
        self.horizontalLayout = QtWidgets.QHBoxLayout(AdvancedSearchSubPanel)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(16)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.fieldComboBox = QtWidgets.QComboBox(AdvancedSearchSubPanel)
        self.fieldComboBox.setObjectName("fieldComboBox")
        self.fieldComboBox.addItem("")
        self.fieldComboBox.addItem("")
        self.fieldComboBox.addItem("")
        self.fieldComboBox.addItem("")
        self.horizontalLayout.addWidget(self.fieldComboBox)
        self.operatorComboBox = QtWidgets.QComboBox(AdvancedSearchSubPanel)
        self.operatorComboBox.setObjectName("operatorComboBox")
        self.horizontalLayout.addWidget(self.operatorComboBox)
        self.operand1LineEdit = QtWidgets.QLineEdit(AdvancedSearchSubPanel)
        self.operand1LineEdit.setInputMethodHints(QtCore.Qt.ImhDate)
        self.operand1LineEdit.setObjectName("operand1LineEdit")
        self.horizontalLayout.addWidget(self.operand1LineEdit)
        self.andLabel = QtWidgets.QLabel(AdvancedSearchSubPanel)
        self.andLabel.setObjectName("andLabel")
        self.horizontalLayout.addWidget(self.andLabel)
        self.operand2LineEdit = QtWidgets.QLineEdit(AdvancedSearchSubPanel)
        self.operand2LineEdit.setInputMethodHints(QtCore.Qt.ImhDate)
        self.operand2LineEdit.setObjectName("operand2LineEdit")
        self.horizontalLayout.addWidget(self.operand2LineEdit)

        self.retranslateUi(AdvancedSearchSubPanel)
        QtCore.QMetaObject.connectSlotsByName(AdvancedSearchSubPanel)

    def retranslateUi(self, AdvancedSearchSubPanel):
        _translate = QtCore.QCoreApplication.translate
        AdvancedSearchSubPanel.setWindowTitle(_translate("AdvancedSearchSubPanel", "Form"))
        self.fieldComboBox.setItemText(0, _translate("AdvancedSearchSubPanel", "Date"))
        self.fieldComboBox.setItemText(1, _translate("AdvancedSearchSubPanel", "Lieu"))
        self.fieldComboBox.setItemText(2, _translate("AdvancedSearchSubPanel", "Nom"))
        self.fieldComboBox.setItemText(3, _translate("AdvancedSearchSubPanel", "Tags"))
        self.andLabel.setText(_translate("AdvancedSearchSubPanel", "et"))

