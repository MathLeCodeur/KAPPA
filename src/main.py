import debug
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication

import config
from kappa.dao.ConnectionManager import *
from kappa.ui.main_window import MainWindow

from kappa.face_detection.inference_image_face import *

def main():
    app = QApplication(sys.argv)
    config.loadThemes(app, False)

    faceDetector = TensorflowFaceDetector()

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
    ConnectionManager.instance.closeConnection()

if __name__ == '__main__':
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    main()
