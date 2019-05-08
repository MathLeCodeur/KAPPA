import sys

from PyQt5.QtCore import *

from ui.main_window import *

def main():
    app = QApplication(sys.argv)
    config.load_themes(app)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
