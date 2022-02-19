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

import os

# Import Qt
from qt_core import *

class MenuPushButton(QPushButton):
    def __init__(
        self,
        text = "",
        font = "10pt 'Consolas'; color: #D0D0D0",
        height = 40,
        minimum_width = 40,
        text_padding = 50,
        icon_path = "",
        icon_color = "#D0D0D0",
        btn_color = "#404040",
        btn_color_hover = "#505050",
        btb_color_press = "#303030",
        is_active = False
    ):
        super().__init__()

        # set default parameters
        self.setText(text)
        self.setMaximumHeight(height)
        self.setMinimumHeight(height)
        self.setCursor(Qt.PointingHandCursor)

        # custom parameters
        self.minimum_width = minimum_width
        self.text_padding = text_padding
        self.icon_path = icon_path
        self.icon_color = icon_color
        self.btn_color = btn_color
        self.btn_color_hover = btn_color_hover
        self.btn_color_press = btb_color_press
        self.is_active = is_active
        self.btn_font = font

        self.set_style()

    def set_active(self, new_state):
        self.is_active = new_state
        self.set_style()

    def set_style(self):

        style = f"""
        QPushButton {{
            font: {self.btn_font};
            background-color: {self.btn_color};
            padding-left: {self.text_padding}px;
            text-align: left;
            border: none;
        }}

        QPushButton:hover {{
            background-color: {self.btn_color_hover};
        }}
        
        QPushButton:pressed {{
            background-color: {self.btn_color_press};
        }}

        """

        active_style = f"""
        QPushButton {{
            background-color: {self.btn_color_hover};
            border-right: 5px solid {self.btn_color_press};
        }}

        """

        if not self.is_active:
            self.setStyleSheet(style)
        else:
            self.setStyleSheet(style + active_style)
    

    def paintEvent(self, event):

        # Return default style
        QPushButton.paintEvent(self, event)

        # Painter
        qp = QPainter()
        qp.begin(self)
        qp.setRenderHint(QPainter.SmoothPixmapTransform)
        qp.setPen(Qt.NoPen)

        rect = QRect(0,0, self.minimum_width, self.height())

        self.draw_icon(qp, self.icon_path, rect, self.icon_color)

        qp.end()


    def draw_icon(self, qp, image, rect, color):

        # Format Path
        app_path = os.path.abspath(os.getcwd())
        folder = "images/icons"
        path = os.path.join(app_path, folder)
        icon_path = os.path.normpath(os.path.join(path, image))

        # Draw icon
        icon = QPixmap(icon_path)
        painter = QPainter(icon)
        painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
        painter.fillRect(icon.rect(), color)
        qp.drawPixmap(
            (rect.width() - icon.width()) / 2,
            (rect.height() - icon.height()) / 2,
            icon
        )
        painter.end()