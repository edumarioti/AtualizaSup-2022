#-------------------------------------------------------------------------------
#
# By: Eduardo Marioti Vargas
# Project made with: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
#-------------------------------------------------------------------------------

# Import Modules
import sys, os 

# Import Qt
from qt_core import *

# Import Windows 
from gui.windows.main_window.ui_main_window import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("AtualizaSup")

        # Setup main window
        self.ui = Ui_MainWindow()
        self.ui.setup_ui(self)

        # Show aplication
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())

