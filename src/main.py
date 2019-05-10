import sys

from PyQt5.QtCore import *

from kappa.face_detection.inference_image_face import *
from kappa.ui.main_window import *

def main():
    app = QApplication(sys.argv)
    config.loadThemes(app, False)

    faceDetector = TensorflowFaceDetector()

    window = MainWindow(faceDetector)
    window.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
