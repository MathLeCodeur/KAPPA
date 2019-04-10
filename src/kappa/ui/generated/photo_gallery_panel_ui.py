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
        self.search_textedit = QtWidgets.QTextEdit(PhotoGalleryPanel)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_textedit.sizePolicy().hasHeightForWidth())
        self.search_textedit.setSizePolicy(sizePolicy)
        self.search_textedit.setMaximumSize(QtCore.QSize(300, 16777215))
        self.search_textedit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.search_textedit.setObjectName("search_textedit")
        self.header.addWidget(self.search_textedit)
        self.search_button = QtWidgets.QPushButton(PhotoGalleryPanel)
        self.search_button.setObjectName("search_button")
        self.header.addWidget(self.search_button)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.header.addItem(spacerItem)
        self.sorting_button = QtWidgets.QPushButton(PhotoGalleryPanel)
        self.sorting_button.setObjectName("sorting_button")
        self.header.addWidget(self.sorting_button)
        self.advanced_search_button = QtWidgets.QPushButton(PhotoGalleryPanel)
        self.advanced_search_button.setObjectName("advanced_search_button")
        self.header.addWidget(self.advanced_search_button)
        self.show_all_button = QtWidgets.QPushButton(PhotoGalleryPanel)
        self.show_all_button.setObjectName("show_all_button")
        self.header.addWidget(self.show_all_button)
        self._2.addLayout(self.header)
        self.scroll_area = QtWidgets.QScrollArea(PhotoGalleryPanel)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scroll_area.sizePolicy().hasHeightForWidth())
        self.scroll_area.setSizePolicy(sizePolicy)
        self.scroll_area.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setObjectName("scroll_area")
        self.content = QtWidgets.QWidget()
        self.content.setGeometry(QtCore.QRect(0, 0, 966, 4390))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.content.sizePolicy().hasHeightForWidth())
        self.content.setSizePolicy(sizePolicy)
        self.content.setObjectName("content")
        self.content_layout = QtWidgets.QVBoxLayout(self.content)
        self.content_layout.setContentsMargins(0, 0, 0, 0)
        self.content_layout.setObjectName("content_layout")
        self.photo_list_view = PhotoListView(self.content)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.photo_list_view.sizePolicy().hasHeightForWidth())
        self.photo_list_view.setSizePolicy(sizePolicy)
        self.photo_list_view.setObjectName("photo_list_view")
        self.content_layout.addWidget(self.photo_list_view)
        self.scroll_area.setWidget(self.content)
        self._2.addWidget(self.scroll_area)

        self.retranslateUi(PhotoGalleryPanel)
        QtCore.QMetaObject.connectSlotsByName(PhotoGalleryPanel)

    def retranslateUi(self, PhotoGalleryPanel):
        _translate = QtCore.QCoreApplication.translate
        self.search_button.setText(_translate("PhotoGalleryPanel", "Search"))
        self.sorting_button.setText(_translate("PhotoGalleryPanel", "Classement"))
        self.advanced_search_button.setText(_translate("PhotoGalleryPanel", "Recherche avancée"))
        self.show_all_button.setText(_translate("PhotoGalleryPanel", "Afficher tout"))

from ui.widgets.photo_list_view import PhotoListView
