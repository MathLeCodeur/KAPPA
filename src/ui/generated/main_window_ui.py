# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'res/ui/main_window.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 700)
        MainWindow.setStyleSheet("")
        self.central_widget = QtWidgets.QWidget(MainWindow)
        self.central_widget.setObjectName("central_widget")
        self.central_widget_layout = QtWidgets.QHBoxLayout(self.central_widget)
        self.central_widget_layout.setContentsMargins(0, 0, 0, 0)
        self.central_widget_layout.setObjectName("central_widget_layout")
        self.stacked_widget = QtWidgets.QStackedWidget(self.central_widget)
        self.stacked_widget.setObjectName("stacked_widget")
        self.central_widget_layout.addWidget(self.stacked_widget)
        MainWindow.setCentralWidget(self.central_widget)
        self.menu_bar = QtWidgets.QMenuBar(MainWindow)
        self.menu_bar.setGeometry(QtCore.QRect(0, 0, 1000, 22))
        self.menu_bar.setObjectName("menu_bar")
        self.file_menu = QtWidgets.QMenu(self.menu_bar)
        self.file_menu.setObjectName("file_menu")
        self.edit_menu = QtWidgets.QMenu(self.menu_bar)
        self.edit_menu.setObjectName("edit_menu")
        self.help_menu = QtWidgets.QMenu(self.menu_bar)
        self.help_menu.setObjectName("help_menu")
        self.view_menu = QtWidgets.QMenu(self.menu_bar)
        self.view_menu.setObjectName("view_menu")
        self.images_size_action = QtWidgets.QMenu(self.view_menu)
        self.images_size_action.setObjectName("images_size_action")
        MainWindow.setMenuBar(self.menu_bar)
        self.import_images_action = QtWidgets.QAction(MainWindow)
        self.import_images_action.setObjectName("import_images_action")
        self.preferences_action = QtWidgets.QAction(MainWindow)
        self.preferences_action.setObjectName("preferences_action")
        self.about_action = QtWidgets.QAction(MainWindow)
        self.about_action.setObjectName("about_action")
        self.help_action = QtWidgets.QAction(MainWindow)
        self.help_action.setObjectName("help_action")
        self.action_small_images = QtWidgets.QAction(MainWindow)
        self.action_small_images.setCheckable(True)
        self.action_small_images.setObjectName("action_small_images")
        self.action_medium_images = QtWidgets.QAction(MainWindow)
        self.action_medium_images.setCheckable(True)
        self.action_medium_images.setChecked(True)
        self.action_medium_images.setObjectName("action_medium_images")
        self.action_large_images = QtWidgets.QAction(MainWindow)
        self.action_large_images.setCheckable(True)
        self.action_large_images.setObjectName("action_large_images")
        self.file_menu.addAction(self.import_images_action)
        self.edit_menu.addAction(self.preferences_action)
        self.help_menu.addAction(self.help_action)
        self.help_menu.addAction(self.about_action)
        self.images_size_action.addAction(self.action_small_images)
        self.images_size_action.addAction(self.action_medium_images)
        self.images_size_action.addAction(self.action_large_images)
        self.view_menu.addAction(self.images_size_action.menuAction())
        self.menu_bar.addAction(self.file_menu.menuAction())
        self.menu_bar.addAction(self.edit_menu.menuAction())
        self.menu_bar.addAction(self.view_menu.menuAction())
        self.menu_bar.addAction(self.help_menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Album Photo"))
        self.file_menu.setTitle(_translate("MainWindow", "Fichier"))
        self.edit_menu.setTitle(_translate("MainWindow", "Edition"))
        self.help_menu.setTitle(_translate("MainWindow", "Aide"))
        self.view_menu.setTitle(_translate("MainWindow", "Affichage"))
        self.images_size_action.setTitle(_translate("MainWindow", "Taille des images"))
        self.import_images_action.setText(_translate("MainWindow", "Importer les images depuis..."))
        self.preferences_action.setText(_translate("MainWindow", "Préférences"))
        self.about_action.setText(_translate("MainWindow", "A propos"))
        self.help_action.setText(_translate("MainWindow", "Aide"))
        self.action_small_images.setText(_translate("MainWindow", "Petites"))
        self.action_medium_images.setText(_translate("MainWindow", "Moyennes"))
        self.action_large_images.setText(_translate("MainWindow", "Grandes"))

from . import samples_rc
