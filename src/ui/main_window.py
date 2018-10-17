from PyQt5.QtWidgets import *
from  .generated.main_window_ui import *

def MainWindow():
    window = window = QMainWindow()
    ui = Ui_main_window()
    ui.setupUi(window)
    return window
