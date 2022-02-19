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
from pages.ui_pages import Ui_app_pages
from widgets.menu_push_buttons import MenuPushButton


STANDART_SCREEN_SIZE_X = 800
STANDART_SCREEN_SIZE_Y = 500


BACKGROUND_COLOR = "#303030"
LEFT_MENU_COLOR = "#404040"
TOP_BAR_COLOR = "#202020"
BOTTOM_BAR_COLOR = "#202020"

PROGRESS_BAR_HEIGHT = 20
PROGRESS_BAR_WIDTH = 500

BAR_STANDARD_HEIGHT = 30

STANDARD_SPACER_SIZE = 20


FONT_STANDARD = "font: 10pt 'Consolas'; color: #D0D0D0"
FONT_SMALL = "font: 8pt 'Consolas'; color: #D0D0D0"

PROGRESS_BAR_STYLE = """QProgressBar{
                            background-color: #505050;
                            font: 700 10pt 'Consolas';
                            color: #202020;
                            border: 1px solid #202020;
                            border-radius: 2px;
                            text-align: center;	
                        }
                        QProgressBar::chunk {
                            background-color: #6EF0D2;
                            margin: 0.5px;
                        }"""

# Main Window
class Ui_MainWindow(object):
    def setup_ui(self, parent):
        if not parent.objectName():
            parent.setObjectName("MainWindow")
            
        # Set initial paramters
        parent.resize(STANDART_SCREEN_SIZE_X, STANDART_SCREEN_SIZE_Y)
        parent.setMinimumSize(STANDART_SCREEN_SIZE_X, STANDART_SCREEN_SIZE_Y)
        parent.setMaximumSize(STANDART_SCREEN_SIZE_X,STANDART_SCREEN_SIZE_Y)

        self.left_menu_standard_width = 40
        self.left_menu_extend_width = 180

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
        self.left_menu.setMaximumWidth(self.left_menu_standard_width)
        self.left_menu.setMinimumWidth(self.left_menu_standard_width)

        self.left_menu_layout = QVBoxLayout(self.left_menu)
        self.left_menu_layout.setContentsMargins(0,0,0,0)
        self.left_menu_layout.setSpacing(0)

        self.left_menu_top_frame = QFrame()
        self.left_menu_top_frame.setMinimumHeight(self.left_menu_standard_width)

        self.leff_menu_top_layout = QVBoxLayout(self.left_menu_top_frame)
        self.leff_menu_top_layout.setContentsMargins(0,0,0,0)
        self.leff_menu_top_layout.setSpacing(0)
        
        self.toggle_button = MenuPushButton(
            text="Ocultar Menu",
            icon_path="icon_menu.svg"
            )

        self.button_home = MenuPushButton(
            text="Página Inicial",
            icon_path="icon_home.svg",
            is_active=True
            )

        self.button_settings = MenuPushButton(
            text="Configurações",
            icon_path="icon_settings.svg"
            )

        self.leff_menu_top_layout.addWidget(self.toggle_button)
        self.leff_menu_top_layout.addWidget(self.button_home)
        self.leff_menu_top_layout.addWidget(self.button_settings)
 
        self.left_menu_spacer = QSpacerItem(STANDARD_SPACER_SIZE, STANDARD_SPACER_SIZE, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.left_menu_bottom_frame = QFrame()
        self.left_menu_bottom_frame.setMinimumHeight(self.left_menu_standard_width)
    

        self.leff_menu_bottom_layout = QVBoxLayout(self.left_menu_bottom_frame)
        self.leff_menu_bottom_layout.setContentsMargins(0,0,0,0)
        self.leff_menu_bottom_layout.setSpacing(0)
        
        self.button_about = MenuPushButton(
            text="Sobre",
            icon_path="icon_link.svg"
            )

        self.leff_menu_bottom_layout.addWidget(self.button_about)

        self.left_menu_label_version = QLabel("v1.0")
        self.left_menu_label_version.setAlignment(Qt.AlignCenter)
        self.left_menu_label_version.setMinimumHeight(BAR_STANDARD_HEIGHT)
        self.left_menu_label_version.setMaximumHeight(BAR_STANDARD_HEIGHT)
        self.left_menu_label_version.setStyleSheet(FONT_SMALL)

        self.left_menu_layout.addWidget(self.left_menu_top_frame)
        self.left_menu_layout.addItem(self.left_menu_spacer)
        self.left_menu_layout.addWidget(self.left_menu_bottom_frame)
        self.left_menu_layout.addWidget(self.left_menu_label_version)

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
        self.top_bar.setMaximumHeight(BAR_STANDARD_HEIGHT)
        self.top_bar.setMinimumHeight(BAR_STANDARD_HEIGHT)

        # Top bar layout
        self.top_bar_layout = QHBoxLayout(self.top_bar)
        self.top_bar_layout.setContentsMargins(5,0,5,0)

        
        # Top spacer
        self.top_spacer = QSpacerItem(STANDARD_SPACER_SIZE, STANDARD_SPACER_SIZE, QSizePolicy.Expanding, QSizePolicy.Minimum)

        # Top right label
        self.top_right_label = QLabel("©2022")
        self.top_right_label.setStyleSheet(FONT_SMALL)

        # Top left label
        self.top_left_label = QLabel("| PÁGINA INICIAL")
        self.top_left_label.setStyleSheet(FONT_STANDARD)

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
        self.bottom_bar.setStyleSheet("background-color:" + BOTTOM_BAR_COLOR)
        self.bottom_bar.setMaximumHeight(BAR_STANDARD_HEIGHT)
        self.bottom_bar.setMinimumHeight(BAR_STANDARD_HEIGHT)

        # Bottom bar layout
        self.bottom_bar_layout = QHBoxLayout(self.bottom_bar)
        self.bottom_bar_layout.setContentsMargins(5,0,5,0)

        # Bottom progress bar
        self.bottom_progress_bar = QProgressBar()
        self.bottom_progress_bar.setStyleSheet(PROGRESS_BAR_STYLE)
        self.bottom_progress_bar.setMinimumHeight(PROGRESS_BAR_HEIGHT)
        self.bottom_progress_bar.setMaximumHeight(PROGRESS_BAR_HEIGHT)
        self.bottom_progress_bar.hide()

        # Bottom left label
        self.bottom_left_label = QLabel("Criado por: Eduardo Marioti")
        self.bottom_left_label.setStyleSheet(FONT_STANDARD)

        # Bottom spacer
        self.bottom_spacer = QSpacerItem(STANDARD_SPACER_SIZE, STANDARD_SPACER_SIZE, QSizePolicy.Expanding, QSizePolicy.Minimum)

        # Add to bottom bar
        self.bottom_bar_layout.addWidget(self.bottom_left_label)
        self.bottom_bar_layout.addWidget(self.bottom_progress_bar)
        

        # Add to content
        self.content_layout.addWidget(self.top_bar)
        self.content_layout.addWidget(self.pages)
        self.content_layout.addWidget(self.bottom_bar)

        # Add to app
        self.main_layout.addWidget(self.left_menu)
        self.main_layout.addWidget(self.content)

        parent.setCentralWidget(self.central_frame)

