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
        PhotoGalleryPanel.resize(1000, 700)
        self._2 = QtWidgets.QVBoxLayout(PhotoGalleryPanel)
        self._2.setObjectName("_2")
        self.header = QtWidgets.QHBoxLayout()
        self.header.setObjectName("header")
        self.searchTextEdit = QtWidgets.QTextEdit(PhotoGalleryPanel)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchTextEdit.sizePolicy().hasHeightForWidth())
        self.searchTextEdit.setSizePolicy(sizePolicy)
        self.searchTextEdit.setMaximumSize(QtCore.QSize(300, 16777215))
        self.searchTextEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.searchTextEdit.setObjectName("searchTextEdit")
        self.header.addWidget(self.searchTextEdit)
        self.searchButton = QtWidgets.QPushButton(PhotoGalleryPanel)
        self.searchButton.setObjectName("searchButton")
        self.header.addWidget(self.searchButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.header.addItem(spacerItem)
        self.sortingButton = QtWidgets.QPushButton(PhotoGalleryPanel)
        self.sortingButton.setObjectName("sortingButton")
        self.header.addWidget(self.sortingButton)
        self.advancedSearchButton = QtWidgets.QPushButton(PhotoGalleryPanel)
        self.advancedSearchButton.setObjectName("advancedSearchButton")
        self.header.addWidget(self.advancedSearchButton)
        self.showAllButton = QtWidgets.QPushButton(PhotoGalleryPanel)
        self.showAllButton.setObjectName("showAllButton")
        self.header.addWidget(self.showAllButton)
        self._2.addLayout(self.header)
        self.scrollArea = QtWidgets.QScrollArea(PhotoGalleryPanel)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.content = QtWidgets.QWidget()
        self.content.setGeometry(QtCore.QRect(0, 0, 980, 647))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.content.sizePolicy().hasHeightForWidth())
        self.content.setSizePolicy(sizePolicy)
        self.content.setObjectName("content")
        self.content_layout = QtWidgets.QVBoxLayout(self.content)
        self.content_layout.setContentsMargins(0, 0, 0, 0)
        self.content_layout.setObjectName("content_layout")
        self.photoListView = PhotoListView(self.content)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.photoListView.sizePolicy().hasHeightForWidth())
        self.photoListView.setSizePolicy(sizePolicy)
        self.photoListView.setObjectName("photoListView")
        self.content_layout.addWidget(self.photoListView)
        self.scrollArea.setWidget(self.content)
        self._2.addWidget(self.scrollArea)

        self.retranslateUi(PhotoGalleryPanel)
        QtCore.QMetaObject.connectSlotsByName(PhotoGalleryPanel)

    def retranslateUi(self, PhotoGalleryPanel):
        _translate = QtCore.QCoreApplication.translate
        self.searchButton.setText(_translate("PhotoGalleryPanel", "Search"))
        self.sortingButton.setText(_translate("PhotoGalleryPanel", "Classement"))
        self.advancedSearchButton.setText(_translate("PhotoGalleryPanel", "Recherche avancée"))
        self.showAllButton.setText(_translate("PhotoGalleryPanel", "Afficher tout"))

from ui.widgets.photo_list_view import PhotoListView
