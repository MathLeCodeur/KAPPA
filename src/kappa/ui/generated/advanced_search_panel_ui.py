# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'res/ui/advanced_search_panel.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AdvancedSearchPanel(object):
    def setupUi(self, AdvancedSearchPanel):
        AdvancedSearchPanel.setObjectName("AdvancedSearchPanel")
        AdvancedSearchPanel.resize(650, 400)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AdvancedSearchPanel.sizePolicy().hasHeightForWidth())
        AdvancedSearchPanel.setSizePolicy(sizePolicy)
        AdvancedSearchPanel.setMinimumSize(QtCore.QSize(650, 400))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./res/icons/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AdvancedSearchPanel.setWindowIcon(icon)
        self.advancedSearchPanelLayout = QtWidgets.QVBoxLayout(AdvancedSearchPanel)
        self.advancedSearchPanelLayout.setContentsMargins(0, 0, 0, 0)
        self.advancedSearchPanelLayout.setSpacing(0)
        self.advancedSearchPanelLayout.setObjectName("advancedSearchPanelLayout")
        self.content = QtWidgets.QFrame(AdvancedSearchPanel)
        self.content.setObjectName("content")
        self.contentLayout = QtWidgets.QVBoxLayout(self.content)
        self.contentLayout.setContentsMargins(24, 24, 24, 24)
        self.contentLayout.setSpacing(24)
        self.contentLayout.setObjectName("contentLayout")
        self.titleAndButtonsContainer = QtWidgets.QHBoxLayout()
        self.titleAndButtonsContainer.setSpacing(12)
        self.titleAndButtonsContainer.setObjectName("titleAndButtonsContainer")
        self.advancedSearchTitleLabel = QtWidgets.QLabel(self.content)
        self.advancedSearchTitleLabel.setObjectName("advancedSearchTitleLabel")
        self.titleAndButtonsContainer.addWidget(self.advancedSearchTitleLabel)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.titleAndButtonsContainer.addItem(spacerItem)
        self.addSmallActionButton = QtWidgets.QPushButton(self.content)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addSmallActionButton.sizePolicy().hasHeightForWidth())
        self.addSmallActionButton.setSizePolicy(sizePolicy)
        self.addSmallActionButton.setMinimumSize(QtCore.QSize(32, 32))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./res/icons/cache/plus.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addSmallActionButton.setIcon(icon1)
        self.addSmallActionButton.setObjectName("addSmallActionButton")
        self.titleAndButtonsContainer.addWidget(self.addSmallActionButton)
        self.removeSmallActionButton = QtWidgets.QPushButton(self.content)
        self.removeSmallActionButton.setEnabled(False)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./res/icons/cache/minus.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.removeSmallActionButton.setIcon(icon2)
        self.removeSmallActionButton.setObjectName("removeSmallActionButton")
        self.titleAndButtonsContainer.addWidget(self.removeSmallActionButton)
        self.contentLayout.addLayout(self.titleAndButtonsContainer)
        self.searchConditionsEmphasisContainer = QtWidgets.QWidget(self.content)
        self.searchConditionsEmphasisContainer.setObjectName("searchConditionsEmphasisContainer")
        self.searchConditionsContainerLayout = QtWidgets.QVBoxLayout(self.searchConditionsEmphasisContainer)
        self.searchConditionsContainerLayout.setContentsMargins(32, 24, 32, 24)
        self.searchConditionsContainerLayout.setSpacing(32)
        self.searchConditionsContainerLayout.setObjectName("searchConditionsContainerLayout")
        self.searchConditionContainer = QtWidgets.QHBoxLayout()
        self.searchConditionContainer.setSpacing(12)
        self.searchConditionContainer.setObjectName("searchConditionContainer")
        self.searchConditionsContainerLayout.addLayout(self.searchConditionContainer)
        self.contentLayout.addWidget(self.searchConditionsEmphasisContainer)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.contentLayout.addItem(spacerItem1)
        self.buttonsOkCancelContainer = QtWidgets.QHBoxLayout()
        self.buttonsOkCancelContainer.setSpacing(10)
        self.buttonsOkCancelContainer.setObjectName("buttonsOkCancelContainer")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.buttonsOkCancelContainer.addItem(spacerItem2)
        self.okButton = QtWidgets.QPushButton(self.content)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.okButton.sizePolicy().hasHeightForWidth())
        self.okButton.setSizePolicy(sizePolicy)
        self.okButton.setMinimumSize(QtCore.QSize(32, 32))
        self.okButton.setObjectName("okButton")
        self.buttonsOkCancelContainer.addWidget(self.okButton)
        self.cancelButton = QtWidgets.QPushButton(self.content)
        self.cancelButton.setMinimumSize(QtCore.QSize(32, 32))
        self.cancelButton.setObjectName("cancelButton")
        self.buttonsOkCancelContainer.addWidget(self.cancelButton)
        self.contentLayout.addLayout(self.buttonsOkCancelContainer)
        self.advancedSearchPanelLayout.addWidget(self.content)

        self.retranslateUi(AdvancedSearchPanel)
        QtCore.QMetaObject.connectSlotsByName(AdvancedSearchPanel)

    def retranslateUi(self, AdvancedSearchPanel):
        _translate = QtCore.QCoreApplication.translate
        AdvancedSearchPanel.setWindowTitle(_translate("AdvancedSearchPanel", "Album Photo - Recherche avancée"))
        self.advancedSearchTitleLabel.setText(_translate("AdvancedSearchPanel", "Critères de recherche"))
        self.addSmallActionButton.setToolTip(_translate("AdvancedSearchPanel", "Ajouter un critère de recherche"))
        self.removeSmallActionButton.setToolTip(_translate("AdvancedSearchPanel", "Supprimer le dernier critère de recherche"))
        self.okButton.setText(_translate("AdvancedSearchPanel", "OK"))
        self.cancelButton.setText(_translate("AdvancedSearchPanel", "Cancel"))

