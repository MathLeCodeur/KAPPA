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
        MainWindow.resize(1200, 900)
        MainWindow.setStyleSheet("")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.central_widget_layout = QtWidgets.QHBoxLayout(self.centralWidget)
        self.central_widget_layout.setContentsMargins(0, 0, 0, 0)
        self.central_widget_layout.setObjectName("central_widget_layout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralWidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.central_widget_layout.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1200, 22))
        self.menuBar.setObjectName("menuBar")
        self.fileMenu = QtWidgets.QMenu(self.menuBar)
        self.fileMenu.setObjectName("fileMenu")
        self.editMenu = QtWidgets.QMenu(self.menuBar)
        self.editMenu.setObjectName("editMenu")
        self.helpMenu = QtWidgets.QMenu(self.menuBar)
        self.helpMenu.setObjectName("helpMenu")
        self.viewMenu = QtWidgets.QMenu(self.menuBar)
        self.viewMenu.setObjectName("viewMenu")
        self.changeIimagesSizeAction = QtWidgets.QMenu(self.viewMenu)
        self.changeIimagesSizeAction.setObjectName("changeIimagesSizeAction")
        MainWindow.setMenuBar(self.menuBar)
        self.importImagesAction = QtWidgets.QAction(MainWindow)
        self.importImagesAction.setObjectName("importImagesAction")
        self.preferencesAction = QtWidgets.QAction(MainWindow)
        self.preferencesAction.setObjectName("preferencesAction")
        self.aboutAction = QtWidgets.QAction(MainWindow)
        self.aboutAction.setObjectName("aboutAction")
        self.helpAction = QtWidgets.QAction(MainWindow)
        self.helpAction.setObjectName("helpAction")
        self.actionSmallImages = QtWidgets.QAction(MainWindow)
        self.actionSmallImages.setCheckable(True)
        self.actionSmallImages.setObjectName("actionSmallImages")
        self.actionMediumImages = QtWidgets.QAction(MainWindow)
        self.actionMediumImages.setCheckable(True)
        self.actionMediumImages.setChecked(True)
        self.actionMediumImages.setObjectName("actionMediumImages")
        self.actionLargeImages = QtWidgets.QAction(MainWindow)
        self.actionLargeImages.setCheckable(True)
        self.actionLargeImages.setObjectName("actionLargeImages")
        self.fileMenu.addAction(self.importImagesAction)
        self.editMenu.addAction(self.preferencesAction)
        self.helpMenu.addAction(self.helpAction)
        self.helpMenu.addAction(self.aboutAction)
        self.changeIimagesSizeAction.addAction(self.actionSmallImages)
        self.changeIimagesSizeAction.addAction(self.actionMediumImages)
        self.changeIimagesSizeAction.addAction(self.actionLargeImages)
        self.viewMenu.addAction(self.changeIimagesSizeAction.menuAction())
        self.menuBar.addAction(self.fileMenu.menuAction())
        self.menuBar.addAction(self.editMenu.menuAction())
        self.menuBar.addAction(self.viewMenu.menuAction())
        self.menuBar.addAction(self.helpMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Album Photo"))
        self.fileMenu.setTitle(_translate("MainWindow", "Fichier"))
        self.editMenu.setTitle(_translate("MainWindow", "Edition"))
        self.helpMenu.setTitle(_translate("MainWindow", "Aide"))
        self.viewMenu.setTitle(_translate("MainWindow", "Affichage"))
        self.changeIimagesSizeAction.setTitle(_translate("MainWindow", "Taille des images"))
        self.importImagesAction.setText(_translate("MainWindow", "Importer les images depuis..."))
        self.preferencesAction.setText(_translate("MainWindow", "Préférences"))
        self.aboutAction.setText(_translate("MainWindow", "A propos"))
        self.helpAction.setText(_translate("MainWindow", "Aide"))
        self.actionSmallImages.setText(_translate("MainWindow", "Petites"))
        self.actionMediumImages.setText(_translate("MainWindow", "Moyennes"))
        self.actionLargeImages.setText(_translate("MainWindow", "Grandes"))

