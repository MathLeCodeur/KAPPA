# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'res/ui/photo_viewer_panel.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PhotoViewerPanel(object):
    def setupUi(self, PhotoViewerPanel):
        PhotoViewerPanel.setObjectName("PhotoViewerPanel")
        PhotoViewerPanel.resize(1000, 700)
        self.photo_viewer_layout = QtWidgets.QVBoxLayout(PhotoViewerPanel)
        self.photo_viewer_layout.setContentsMargins(0, 0, 0, 0)
        self.photo_viewer_layout.setSpacing(0)
        self.photo_viewer_layout.setObjectName("photo_viewer_layout")
        self.header = QtWidgets.QWidget(PhotoViewerPanel)
        self.header.setObjectName("header")
        self.headerLayout = QtWidgets.QHBoxLayout(self.header)
        self.headerLayout.setContentsMargins(0, 0, 0, 0)
        self.headerLayout.setSpacing(0)
        self.headerLayout.setObjectName("headerLayout")
        self.backActionButton = QtWidgets.QPushButton(self.header)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./res/icons/cache/back_arrow.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.backActionButton.setIcon(icon)
        self.backActionButton.setObjectName("backActionButton")
        self.headerLayout.addWidget(self.backActionButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.headerLayout.addItem(spacerItem)
        self.adjustZoomActionButton = QtWidgets.QPushButton(self.header)
        self.adjustZoomActionButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./res/icons/cache/zoom_in.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.adjustZoomActionButton.setIcon(icon1)
        self.adjustZoomActionButton.setObjectName("adjustZoomActionButton")
        self.headerLayout.addWidget(self.adjustZoomActionButton)
        self.deleteActionButton = QtWidgets.QPushButton(self.header)
        self.deleteActionButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./res/icons/cache/delete.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.deleteActionButton.setIcon(icon2)
        self.deleteActionButton.setObjectName("deleteActionButton")
        self.headerLayout.addWidget(self.deleteActionButton)
        self.addToFavouritesActionButton = QtWidgets.QPushButton(self.header)
        self.addToFavouritesActionButton.setEnabled(False)
        self.addToFavouritesActionButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("./res/icons/cache/favorite.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addToFavouritesActionButton.setIcon(icon3)
        self.addToFavouritesActionButton.setObjectName("addToFavouritesActionButton")
        self.headerLayout.addWidget(self.addToFavouritesActionButton)
        self.frameObjectsAndPeopleActionButton = QtWidgets.QPushButton(self.header)
        self.frameObjectsAndPeopleActionButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("./res/icons/cache/face_id.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.frameObjectsAndPeopleActionButton.setIcon(icon4)
        self.frameObjectsAndPeopleActionButton.setObjectName("frameObjectsAndPeopleActionButton")
        self.headerLayout.addWidget(self.frameObjectsAndPeopleActionButton)
        self.searchSimilarActionButton = QtWidgets.QPushButton(self.header)
        self.searchSimilarActionButton.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("./res/icons/cache/related_pictures.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.searchSimilarActionButton.setIcon(icon5)
        self.searchSimilarActionButton.setObjectName("searchSimilarActionButton")
        self.headerLayout.addWidget(self.searchSimilarActionButton)
        self.photo_viewer_layout.addWidget(self.header)
        self.splitterVertical = QtWidgets.QSplitter(PhotoViewerPanel)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.splitterVertical.sizePolicy().hasHeightForWidth())
        self.splitterVertical.setSizePolicy(sizePolicy)
        self.splitterVertical.setOrientation(QtCore.Qt.Vertical)
        self.splitterVertical.setHandleWidth(0)
        self.splitterVertical.setObjectName("splitterVertical")
        self.splitterHorizontal = QtWidgets.QSplitter(self.splitterVertical)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.splitterHorizontal.sizePolicy().hasHeightForWidth())
        self.splitterHorizontal.setSizePolicy(sizePolicy)
        self.splitterHorizontal.setOrientation(QtCore.Qt.Horizontal)
        self.splitterHorizontal.setHandleWidth(0)
        self.splitterHorizontal.setObjectName("splitterHorizontal")
        self.imageInfoRootContainer = QtWidgets.QWidget(self.splitterHorizontal)
        self.imageInfoRootContainer.setMaximumSize(QtCore.QSize(300, 16777215))
        self.imageInfoRootContainer.setObjectName("imageInfoRootContainer")
        self.imageInfoRootContainerLayout = QtWidgets.QVBoxLayout(self.imageInfoRootContainer)
        self.imageInfoRootContainerLayout.setContentsMargins(24, 24, 24, 24)
        self.imageInfoRootContainerLayout.setSpacing(24)
        self.imageInfoRootContainerLayout.setObjectName("imageInfoRootContainerLayout")
        self.imageInfoTitleLabel = QtWidgets.QLabel(self.imageInfoRootContainer)
        self.imageInfoTitleLabel.setObjectName("imageInfoTitleLabel")
        self.imageInfoRootContainerLayout.addWidget(self.imageInfoTitleLabel)
        self.imageInfoScrollArea = QtWidgets.QScrollArea(self.imageInfoRootContainer)
        self.imageInfoScrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.imageInfoScrollArea.setWidgetResizable(True)
        self.imageInfoScrollArea.setObjectName("imageInfoScrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 250, 460))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollAreaWidgetContentsLayout = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.scrollAreaWidgetContentsLayout.setContentsMargins(0, 0, 0, 0)
        self.scrollAreaWidgetContentsLayout.setSpacing(0)
        self.scrollAreaWidgetContentsLayout.setObjectName("scrollAreaWidgetContentsLayout")
        self.imageInfoContainer = QtWidgets.QVBoxLayout()
        self.imageInfoContainer.setSpacing(20)
        self.imageInfoContainer.setObjectName("imageInfoContainer")
        self.imageNameContainer = QtWidgets.QVBoxLayout()
        self.imageNameContainer.setSpacing(2)
        self.imageNameContainer.setObjectName("imageNameContainer")
        self.imageNameFieldLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.imageNameFieldLabel.setObjectName("imageNameFieldLabel")
        self.imageNameContainer.addWidget(self.imageNameFieldLabel)
        self.imageNameValueLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.imageNameValueLabel.setText("")
        self.imageNameValueLabel.setObjectName("imageNameValueLabel")
        self.imageNameContainer.addWidget(self.imageNameValueLabel)
        self.imageInfoContainer.addLayout(self.imageNameContainer)
        self.imageDateContainer = QtWidgets.QVBoxLayout()
        self.imageDateContainer.setSpacing(2)
        self.imageDateContainer.setObjectName("imageDateContainer")
        self.imageDateFieldLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.imageDateFieldLabel.setObjectName("imageDateFieldLabel")
        self.imageDateContainer.addWidget(self.imageDateFieldLabel)
        self.imageDateValueLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.imageDateValueLabel.setText("")
        self.imageDateValueLabel.setObjectName("imageDateValueLabel")
        self.imageDateContainer.addWidget(self.imageDateValueLabel)
        self.imageInfoContainer.addLayout(self.imageDateContainer)
        self.imageSizeContainer = QtWidgets.QVBoxLayout()
        self.imageSizeContainer.setSpacing(2)
        self.imageSizeContainer.setObjectName("imageSizeContainer")
        self.imageSizeFieldLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.imageSizeFieldLabel.setObjectName("imageSizeFieldLabel")
        self.imageSizeContainer.addWidget(self.imageSizeFieldLabel)
        self.imageSizeValueLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.imageSizeValueLabel.setText("")
        self.imageSizeValueLabel.setObjectName("imageSizeValueLabel")
        self.imageSizeContainer.addWidget(self.imageSizeValueLabel)
        self.imageInfoContainer.addLayout(self.imageSizeContainer)
        self.imageDimensionsContainer = QtWidgets.QVBoxLayout()
        self.imageDimensionsContainer.setSpacing(2)
        self.imageDimensionsContainer.setObjectName("imageDimensionsContainer")
        self.imageDimensionsFieldLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.imageDimensionsFieldLabel.setObjectName("imageDimensionsFieldLabel")
        self.imageDimensionsContainer.addWidget(self.imageDimensionsFieldLabel)
        self.imageDimensionsValueLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.imageDimensionsValueLabel.setText("")
        self.imageDimensionsValueLabel.setObjectName("imageDimensionsValueLabel")
        self.imageDimensionsContainer.addWidget(self.imageDimensionsValueLabel)
        self.imageInfoContainer.addLayout(self.imageDimensionsContainer)
        self.imagePathContainer = QtWidgets.QVBoxLayout()
        self.imagePathContainer.setSpacing(2)
        self.imagePathContainer.setObjectName("imagePathContainer")
        self.imagePathFieldLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.imagePathFieldLabel.setObjectName("imagePathFieldLabel")
        self.imagePathContainer.addWidget(self.imagePathFieldLabel)
        self.imagePathValueLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.imagePathValueLabel.setText("")
        self.imagePathValueLabel.setObjectName("imagePathValueLabel")
        self.imagePathContainer.addWidget(self.imagePathValueLabel)
        self.imageInfoContainer.addLayout(self.imagePathContainer)
        self.imageTagsContainer = QtWidgets.QVBoxLayout()
        self.imageTagsContainer.setSpacing(2)
        self.imageTagsContainer.setObjectName("imageTagsContainer")
        self.imageTagsFieldLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.imageTagsFieldLabel.setObjectName("imageTagsFieldLabel")
        self.imageTagsContainer.addWidget(self.imageTagsFieldLabel)
        self.imageTagsValueLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.imageTagsValueLabel.setObjectName("imageTagsValueLabel")
        self.imageTagsContainer.addWidget(self.imageTagsValueLabel)
        self.imageInfoContainer.addLayout(self.imageTagsContainer)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.imageInfoContainer.addItem(spacerItem1)
        self.scrollAreaWidgetContentsLayout.addLayout(self.imageInfoContainer)
        self.imageInfoScrollArea.setWidget(self.scrollAreaWidgetContents)
        self.imageInfoRootContainerLayout.addWidget(self.imageInfoScrollArea)
        self.imageContainer = QtWidgets.QWidget(self.splitterHorizontal)
        self.imageContainer.setObjectName("imageContainer")
        self.imageContainerLayout = QtWidgets.QVBoxLayout(self.imageContainer)
        self.imageContainerLayout.setContentsMargins(32, 32, 32, 32)
        self.imageContainerLayout.setObjectName("imageContainerLayout")
        self.image = PhotoView(self.imageContainer)
        self.image.setObjectName("image")
        self.imageContainerLayout.addWidget(self.image)
        self.scrollAreaSimilarImages = QtWidgets.QScrollArea(self.splitterVertical)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaSimilarImages.sizePolicy().hasHeightForWidth())
        self.scrollAreaSimilarImages.setSizePolicy(sizePolicy)
        self.scrollAreaSimilarImages.setMinimumSize(QtCore.QSize(0, 128))
        self.scrollAreaSimilarImages.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollAreaSimilarImages.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollAreaSimilarImages.setWidgetResizable(True)
        self.scrollAreaSimilarImages.setObjectName("scrollAreaSimilarImages")
        self.similarImagesParentContainer = QtWidgets.QWidget()
        self.similarImagesParentContainer.setObjectName("similarImagesParentContainer")
        self.similarImagesParentLayout = QtWidgets.QHBoxLayout(self.similarImagesParentContainer)
        self.similarImagesParentLayout.setContentsMargins(0, 0, 0, 0)
        self.similarImagesParentLayout.setObjectName("similarImagesParentLayout")
        self.similarImagesContainer = QtWidgets.QWidget(self.similarImagesParentContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.similarImagesContainer.sizePolicy().hasHeightForWidth())
        self.similarImagesContainer.setSizePolicy(sizePolicy)
        self.similarImagesContainer.setObjectName("similarImagesContainer")
        self.similarImagesLayout = QtWidgets.QHBoxLayout(self.similarImagesContainer)
        self.similarImagesLayout.setContentsMargins(8, 8, 8, 8)
        self.similarImagesLayout.setObjectName("similarImagesLayout")
        self.similarImagesParentLayout.addWidget(self.similarImagesContainer)
        self.scrollAreaSimilarImages.setWidget(self.similarImagesParentContainer)
        self.photo_viewer_layout.addWidget(self.splitterVertical)

        self.retranslateUi(PhotoViewerPanel)
        QtCore.QMetaObject.connectSlotsByName(PhotoViewerPanel)

    def retranslateUi(self, PhotoViewerPanel):
        _translate = QtCore.QCoreApplication.translate
        self.backActionButton.setToolTip(_translate("PhotoViewerPanel", "Retour"))
        self.adjustZoomActionButton.setToolTip(_translate("PhotoViewerPanel", "Ajuster le niveau de zoom"))
        self.deleteActionButton.setToolTip(_translate("PhotoViewerPanel", "Supprimer"))
        self.addToFavouritesActionButton.setToolTip(_translate("PhotoViewerPanel", "Ajouter aux favoris"))
        self.frameObjectsAndPeopleActionButton.setToolTip(_translate("PhotoViewerPanel", "Encadrer les objets et les visages reconnus"))
        self.searchSimilarActionButton.setToolTip(_translate("PhotoViewerPanel", "Images similaires"))
        self.imageInfoTitleLabel.setText(_translate("PhotoViewerPanel", "Informations"))
        self.imageNameFieldLabel.setText(_translate("PhotoViewerPanel", "Nom"))
        self.imageDateFieldLabel.setText(_translate("PhotoViewerPanel", "Date de prise"))
        self.imageSizeFieldLabel.setText(_translate("PhotoViewerPanel", "Taille"))
        self.imageDimensionsFieldLabel.setText(_translate("PhotoViewerPanel", "Dimensions"))
        self.imagePathFieldLabel.setText(_translate("PhotoViewerPanel", "Source"))
        self.imageTagsFieldLabel.setText(_translate("PhotoViewerPanel", "Tags"))
        self.imageTagsValueLabel.setText(_translate("PhotoViewerPanel", "---"))

from kappa.ui.widgets.photo_view import PhotoView
