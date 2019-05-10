# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'res/ui/photo_gallery_panel.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PhotoGalleryPanel(object):
    def setupUi(self, PhotoGalleryPanel):
        PhotoGalleryPanel.setObjectName("PhotoGalleryPanel")
        PhotoGalleryPanel.resize(1079, 769)
        PhotoGalleryPanel.setStyleSheet("")
        self.photoGalleryPanelLayout = QtWidgets.QVBoxLayout(PhotoGalleryPanel)
        self.photoGalleryPanelLayout.setContentsMargins(0, 0, 0, 0)
        self.photoGalleryPanelLayout.setSpacing(0)
        self.photoGalleryPanelLayout.setObjectName("photoGalleryPanelLayout")
        self.header = QtWidgets.QWidget(PhotoGalleryPanel)
        self.header.setObjectName("header")
        self.headerLayout = QtWidgets.QHBoxLayout(self.header)
        self.headerLayout.setContentsMargins(120, 0, 0, 0)
        self.headerLayout.setSpacing(0)
        self.headerLayout.setObjectName("headerLayout")
        self.searchLineEdit = QtWidgets.QLineEdit(self.header)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchLineEdit.sizePolicy().hasHeightForWidth())
        self.searchLineEdit.setSizePolicy(sizePolicy)
        self.searchLineEdit.setMinimumSize(QtCore.QSize(260, 32))
        self.searchLineEdit.setMaximumSize(QtCore.QSize(396, 16777215))
        self.searchLineEdit.setObjectName("searchLineEdit")
        self.headerLayout.addWidget(self.searchLineEdit)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.headerLayout.addItem(spacerItem)
        self.groupByContainer = QtWidgets.QHBoxLayout()
        self.groupByContainer.setContentsMargins(16, -1, 16, -1)
        self.groupByContainer.setSpacing(16)
        self.groupByContainer.setObjectName("groupByContainer")
        self.groupBySmallLabel = QtWidgets.QLabel(self.header)
        self.groupBySmallLabel.setObjectName("groupBySmallLabel")
        self.groupByContainer.addWidget(self.groupBySmallLabel)
        self.groupByComboBox = QtWidgets.QComboBox(self.header)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupByComboBox.sizePolicy().hasHeightForWidth())
        self.groupByComboBox.setSizePolicy(sizePolicy)
        self.groupByComboBox.setMinimumSize(QtCore.QSize(0, 24))
        self.groupByComboBox.setObjectName("groupByComboBox")
        self.groupByComboBox.addItem("")
        self.groupByComboBox.addItem("")
        self.groupByContainer.addWidget(self.groupByComboBox)
        self.headerLayout.addLayout(self.groupByContainer)
        self.advancedSearchActionButton = QtWidgets.QPushButton(self.header)
        self.advancedSearchActionButton.setMinimumSize(QtCore.QSize(62, 48))
        self.advancedSearchActionButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./res/icons/cache/advanced_search.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.advancedSearchActionButton.setIcon(icon)
        self.advancedSearchActionButton.setIconSize(QtCore.QSize(24, 24))
        self.advancedSearchActionButton.setObjectName("advancedSearchActionButton")
        self.headerLayout.addWidget(self.advancedSearchActionButton)
        self.importFolderActionButton = QtWidgets.QPushButton(self.header)
        self.importFolderActionButton.setMinimumSize(QtCore.QSize(62, 48))
        self.importFolderActionButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./res/icons/cache/import_folder.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.importFolderActionButton.setIcon(icon1)
        self.importFolderActionButton.setIconSize(QtCore.QSize(24, 24))
        self.importFolderActionButton.setObjectName("importFolderActionButton")
        self.headerLayout.addWidget(self.importFolderActionButton)
        self.changeThemeActionButton = QtWidgets.QPushButton(self.header)
        self.changeThemeActionButton.setMinimumSize(QtCore.QSize(62, 48))
        self.changeThemeActionButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./res/icons/cache/change_theme.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.changeThemeActionButton.setIcon(icon2)
        self.changeThemeActionButton.setIconSize(QtCore.QSize(24, 24))
        self.changeThemeActionButton.setObjectName("changeThemeActionButton")
        self.headerLayout.addWidget(self.changeThemeActionButton)
        self.headerLayout.setStretch(0, 1)
        self.photoGalleryPanelLayout.addWidget(self.header)
        self.photoGalleryContainer = QtWidgets.QScrollArea(PhotoGalleryPanel)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.photoGalleryContainer.sizePolicy().hasHeightForWidth())
        self.photoGalleryContainer.setSizePolicy(sizePolicy)
        self.photoGalleryContainer.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.photoGalleryContainer.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.photoGalleryContainer.setWidgetResizable(True)
        self.photoGalleryContainer.setObjectName("photoGalleryContainer")
        self.content = QtWidgets.QWidget()
        self.content.setGeometry(QtCore.QRect(0, 0, 1077, 719))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.content.sizePolicy().hasHeightForWidth())
        self.content.setSizePolicy(sizePolicy)
        self.content.setObjectName("content")
        self.contentLayout = QtWidgets.QVBoxLayout(self.content)
        self.contentLayout.setContentsMargins(120, 32, 120, 0)
        self.contentLayout.setObjectName("contentLayout")
        self.photoListView = PhotoListView(self.content)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.photoListView.sizePolicy().hasHeightForWidth())
        self.photoListView.setSizePolicy(sizePolicy)
        self.photoListView.setObjectName("photoListView")
        self.contentLayout.addWidget(self.photoListView)
        self.photoGalleryContainer.setWidget(self.content)
        self.photoGalleryPanelLayout.addWidget(self.photoGalleryContainer)

        self.retranslateUi(PhotoGalleryPanel)
        QtCore.QMetaObject.connectSlotsByName(PhotoGalleryPanel)

    def retranslateUi(self, PhotoGalleryPanel):
        _translate = QtCore.QCoreApplication.translate
        self.searchLineEdit.setPlaceholderText(_translate("PhotoGalleryPanel", "Recherche par nom, date, tags"))
        self.groupBySmallLabel.setText(_translate("PhotoGalleryPanel", "Grouper par"))
        self.groupByComboBox.setItemText(0, _translate("PhotoGalleryPanel", "Date"))
        self.groupByComboBox.setItemText(1, _translate("PhotoGalleryPanel", "Tag"))
        self.advancedSearchActionButton.setToolTip(_translate("PhotoGalleryPanel", "Recherche avancée"))
        self.importFolderActionButton.setToolTip(_translate("PhotoGalleryPanel", "Importer un répertoire d\'images"))
        self.changeThemeActionButton.setToolTip(_translate("PhotoGalleryPanel", "Changer le thème graphique"))

from kappa.ui.widgets.photo_list_view import PhotoListView
