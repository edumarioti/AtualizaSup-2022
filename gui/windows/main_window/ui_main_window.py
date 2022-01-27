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

# Import Qt
from qt_core import *

# Import pages
from gui.pages.ui_pages import Ui_app_pages


STANDART_SCREEN_SIZE_X = 640
STANDART_SCREEN_SIZE_Y = 370

MINIMUM_SCREEN_SIZE_X = 640
MINIMUM_SCREEN_SIZE_Y = 370

BACKGROUND_COLOR = "#404040"
LEFT_MENU_COLOR = "#202020"
TOP_BAR_COLOR = "#303030"
BOTTOM_BAR_COLOR = "#303030"


LEFT_MENU_STANDARD_WIDTH = 50

TOP_BAR_STANDARD_HEIGHT = 30

STANDARD_SPACER_SIZE = 20


FONT_TOP_BAR = "font: 10pt 'Consolas'; color: #D0D0D0"


# Main Window
class Ui_MainWindow(object):
    def setup_ui(self, parent):
        if not parent.objectName():
            parent.setObjectName("MainWindow")
            
        # Set initial paramters
        parent.resize(STANDART_SCREEN_SIZE_X, STANDART_SCREEN_SIZE_Y)
        parent.setMinimumSize(MINIMUM_SCREEN_SIZE_X, MINIMUM_SCREEN_SIZE_Y)

        # Central Widget 
        self.central_frame = QFrame()
        self.central_frame.setStyleSheet("background-color:" + BACKGROUND_COLOR)

        # Main Layout
        self.main_layout = QHBoxLayout(self.central_frame)
        self.main_layout.setContentsMargins(0,0,0,0)
        self.main_layout.setSpacing(0)

        # Left Menu
        self.left_menu = QFrame()
        self.left_menu.setStyleSheet("background-color:" + LEFT_MENU_COLOR)
        self.left_menu.setMaximumWidth(LEFT_MENU_STANDARD_WIDTH)
        self.left_menu.setMinimumWidth(LEFT_MENU_STANDARD_WIDTH)
        
        # Content
        self.content = QFrame()
        self.content.setStyleSheet("background-color:" + BACKGROUND_COLOR)

        # Content layout
        self.content_layout = QVBoxLayout(self.content)
        self.content_layout.setContentsMargins(0,0,0,0)
        self.content_layout.setSpacing(0)


        # Top bar
        self.top_bar = QFrame()
        self.top_bar.setStyleSheet("background-color:" + TOP_BAR_COLOR)
        self.top_bar.setMaximumHeight(TOP_BAR_STANDARD_HEIGHT)
        self.top_bar.setMinimumHeight(TOP_BAR_STANDARD_HEIGHT)

        # Top bar layout
        self.top_bar_layout = QHBoxLayout(self.top_bar)
        self.top_bar_layout.setContentsMargins(5,0,5,0)

        # Top left label
        self.top_left_label = QLabel("Page 1")
        self.top_left_label.setStyleSheet(FONT_TOP_BAR)
        
        # Top spacer
        self.top_spacer = QSpacerItem(STANDARD_SPACER_SIZE, STANDARD_SPACER_SIZE, QSizePolicy.Expanding, QSizePolicy.Minimum)

        # Top right label
        self.top_right_label = QLabel("| PÁGINA INICIAL")
        self.top_right_label.setStyleSheet(FONT_TOP_BAR)

        # Add to top bar
        self.top_bar_layout.addWidget(self.top_left_label)
        self.top_bar_layout.addItem(self.top_spacer)
        self.top_bar_layout.addWidget(self.top_right_label)


        # App pages
        self.pages = QStackedWidget()
        self.pages.setStyleSheet("background-color:" + BACKGROUND_COLOR)
        self.ui_pages = Ui_app_pages()
        self.ui_pages.setupUi(self.pages)


        # Bottom bar
        self.bottom_bar = QFrame()
        self.bottom_bar.setStyleSheet("background-color:" + TOP_BAR_COLOR)
        self.bottom_bar.setMaximumHeight(TOP_BAR_STANDARD_HEIGHT)
        self.bottom_bar.setMinimumHeight(TOP_BAR_STANDARD_HEIGHT)

        # Bottom bar layout
        self.bottom_bar_layout = QHBoxLayout(self.bottom_bar)
        self.bottom_bar_layout.setContentsMargins(5,0,5,0)

        # Bottom left label
        self.bottom_left_label = QLabel("Criado por: Eduardo Marioti")
        self.bottom_left_label.setStyleSheet(FONT_TOP_BAR)
        
        # Bottom spacer
        self.bottom_spacer = QSpacerItem(STANDARD_SPACER_SIZE, STANDARD_SPACER_SIZE, QSizePolicy.Expanding, QSizePolicy.Minimum)

        # Bottom right label
        self.bottom_right_label = QLabel("© 2022")
        self.bottom_right_label.setStyleSheet(FONT_TOP_BAR)

        # Add to bottom bar
        self.bottom_bar_layout.addWidget(self.bottom_left_label)
        self.bottom_bar_layout.addItem(self.bottom_spacer)
        self.bottom_bar_layout.addWidget(self.bottom_right_label)

        # Add to content
        self.content_layout.addWidget(self.top_bar)
        self.content_layout.addWidget(self.pages)
        self.content_layout.addWidget(self.bottom_bar)

        # Add to app
        self.main_layout.addWidget(self.left_menu)
        self.main_layout.addWidget(self.content)

        parent.setCentralWidget(self.central_frame)

