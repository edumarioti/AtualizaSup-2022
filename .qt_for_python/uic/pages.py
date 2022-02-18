# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pages.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFormLayout, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)

class Ui_app_pages(object):
    def setupUi(self, app_pages):
        if not app_pages.objectName():
            app_pages.setObjectName(u"app_pages")
        app_pages.resize(722, 451)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(app_pages.sizePolicy().hasHeightForWidth())
        app_pages.setSizePolicy(sizePolicy)
        app_pages.setStyleSheet(u"*{\n"
"	font: 10pt \"Consolas\"; \n"
"	color: #D0D0D0;\n"
"	background-color: #303030;\n"
"}\n"
"\n"
"QGroupBox {\n"
"	font: 700 12pt \"Consolas\"; \n"
"	color: #D0D0D0;\n"
"    border: none;\n"
"	border-top: 2px solid #D0D0D0;\n"
"    margin-top: 10px;\n"
"	margin-left: 15px;\n"
"	margin-right: 15px;\n"
"}\n"
"\n"
"QGroupBox::title  {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"	padding: 0px 10px;\n"
"}\n"
"\n"
"QPushButton{\n"
"	background-color: #404040;\n"
"	border: 1px solid #202020;\n"
"	border-radius: 2px;	\n"
"	min-width: 20ex;\n"
"	padding: 3px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: #505050;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: #202020;	\n"
"}\n"
"\n"
"QCheckBox {\n"
"    spacing: 5px;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 9px;\n"
"    height: 9px;\n"
"	background-color: #404040;\n"
"	border: 1px solid #202020;\n"
"	border-radius: 2px;	\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color: #6E"
                        "F0D2;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"	border: 1px solid #6EF0D2;\n"
"}\n"
"\n"
"QCheckBox::indicator:disabled{\n"
"	border: 1px solid #202020;\n"
"	background-color: #303030;\n"
"}\n"
"\n"
"QCheckBox::disabled{\n"
"	color:  #505050;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    border: 1px solid #202020;\n"
"    border-radius: 2px;\n"
"    padding: 0 8px;\n"
"    background: #404040;\n"
"    \n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border-color: #6EF0D2;\n"
"	background: #505050;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"	background: #505050;\n"
"}\n"
"\n"
"QLineEdit[text=\\\"\\\"]{ color:red; }\n"
"\n"
"QLabel#label_tittle_about{\n"
"	font: 700 14pt \"Consolas\";\n"
"}\n"
"\n"
"")
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.verticalLayout = QVBoxLayout(self.page_home)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.group_update = QGroupBox(self.page_home)
        self.group_update.setObjectName(u"group_update")
        self.verticalLayout_4 = QVBoxLayout(self.group_update)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(10, 10, 10, 0)
        self.label_update = QLabel(self.group_update)
        self.label_update.setObjectName(u"label_update")
        self.label_update.setMinimumSize(QSize(0, 0))
        self.label_update.setMaximumSize(QSize(16777215, 16777215))
        self.label_update.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label_update.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.label_update)

        self.frame_optiond_update = QFrame(self.group_update)
        self.frame_optiond_update.setObjectName(u"frame_optiond_update")
        self.frame_optiond_update.setMinimumSize(QSize(0, 80))
        self.frame_optiond_update.setMaximumSize(QSize(16777215, 80))
        self.frame_optiond_update.setFrameShape(QFrame.StyledPanel)
        self.frame_optiond_update.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_optiond_update)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, -1, -1, 0)
        self.check_tag = QCheckBox(self.frame_optiond_update)
        self.check_tag.setObjectName(u"check_tag")

        self.gridLayout.addWidget(self.check_tag, 0, 1, 1, 1)

        self.check_gfx = QCheckBox(self.frame_optiond_update)
        self.check_gfx.setObjectName(u"check_gfx")

        self.gridLayout.addWidget(self.check_gfx, 0, 0, 1, 1)

        self.check_uptade_all = QCheckBox(self.frame_optiond_update)
        self.check_uptade_all.setObjectName(u"check_uptade_all")

        self.gridLayout.addWidget(self.check_uptade_all, 0, 2, 1, 1)

        self.check_datalog = QCheckBox(self.frame_optiond_update)
        self.check_datalog.setObjectName(u"check_datalog")

        self.gridLayout.addWidget(self.check_datalog, 1, 0, 1, 1)

        self.check_users = QCheckBox(self.frame_optiond_update)
        self.check_users.setObjectName(u"check_users")

        self.gridLayout.addWidget(self.check_users, 1, 1, 1, 1)


        self.verticalLayout_4.addWidget(self.frame_optiond_update)

        self.frame_update = QFrame(self.group_update)
        self.frame_update.setObjectName(u"frame_update")
        self.frame_update.setMinimumSize(QSize(0, 100))
        self.frame_update.setMaximumSize(QSize(16777215, 100))
        self.frame_update.setFrameShape(QFrame.StyledPanel)
        self.frame_update.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_update)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, -1, -1, 0)
        self.frame_confirmation = QFrame(self.frame_update)
        self.frame_confirmation.setObjectName(u"frame_confirmation")
        self.frame_confirmation.setMinimumSize(QSize(500, 0))
        self.frame_confirmation.setMaximumSize(QSize(500, 16777215))
        self.frame_confirmation.setFrameShape(QFrame.StyledPanel)
        self.frame_confirmation.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_confirmation)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_confirmation = QLabel(self.frame_confirmation)
        self.label_confirmation.setObjectName(u"label_confirmation")
        self.label_confirmation.setMinimumSize(QSize(0, 0))
        self.label_confirmation.setAlignment(Qt.AlignCenter)
        self.label_confirmation.setWordWrap(True)

        self.verticalLayout_8.addWidget(self.label_confirmation)

        self.frame_buttons_confirmation = QFrame(self.frame_confirmation)
        self.frame_buttons_confirmation.setObjectName(u"frame_buttons_confirmation")
        self.frame_buttons_confirmation.setMaximumSize(QSize(300, 16777215))
        self.frame_buttons_confirmation.setFrameShape(QFrame.StyledPanel)
        self.frame_buttons_confirmation.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_buttons_confirmation)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.button_confirm_uptade = QPushButton(self.frame_buttons_confirmation)
        self.button_confirm_uptade.setObjectName(u"button_confirm_uptade")
        self.button_confirm_uptade.setMaximumSize(QSize(128, 16777215))
        self.button_confirm_uptade.setCheckable(False)

        self.horizontalLayout_4.addWidget(self.button_confirm_uptade)

        self.button_cancel_uptade = QPushButton(self.frame_buttons_confirmation)
        self.button_cancel_uptade.setObjectName(u"button_cancel_uptade")
        self.button_cancel_uptade.setMaximumSize(QSize(128, 16777215))
        self.button_cancel_uptade.setCheckable(False)

        self.horizontalLayout_4.addWidget(self.button_cancel_uptade)


        self.verticalLayout_8.addWidget(self.frame_buttons_confirmation, 0, Qt.AlignHCenter)


        self.horizontalLayout_3.addWidget(self.frame_confirmation)

        self.button_uptade = QPushButton(self.frame_update)
        self.button_uptade.setObjectName(u"button_uptade")
        self.button_uptade.setMaximumSize(QSize(128, 16777215))
        self.button_uptade.setCheckable(False)

        self.horizontalLayout_3.addWidget(self.button_uptade)


        self.verticalLayout_4.addWidget(self.frame_update)


        self.verticalLayout.addWidget(self.group_update)

        self.group_reboot = QGroupBox(self.page_home)
        self.group_reboot.setObjectName(u"group_reboot")
        self.group_reboot.setMinimumSize(QSize(0, 130))
        self.group_reboot.setMaximumSize(QSize(16777215, 130))
        self.verticalLayout_5 = QVBoxLayout(self.group_reboot)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(10, 0, 10, -1)
        self.label_reboot = QLabel(self.group_reboot)
        self.label_reboot.setObjectName(u"label_reboot")
        self.label_reboot.setMinimumSize(QSize(0, 40))
        self.label_reboot.setMaximumSize(QSize(16777215, 40))
        self.label_reboot.setScaledContents(False)
        self.label_reboot.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label_reboot.setWordWrap(True)

        self.verticalLayout_5.addWidget(self.label_reboot)

        self.button_reboot = QPushButton(self.group_reboot)
        self.button_reboot.setObjectName(u"button_reboot")
        self.button_reboot.setStyleSheet(u"")

        self.verticalLayout_5.addWidget(self.button_reboot, 0, Qt.AlignHCenter)


        self.verticalLayout.addWidget(self.group_reboot)

        app_pages.addWidget(self.page_home)
        self.page_settings = QWidget()
        self.page_settings.setObjectName(u"page_settings")
        self.verticalLayout_2 = QVBoxLayout(self.page_settings)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.group_settings = QGroupBox(self.page_settings)
        self.group_settings.setObjectName(u"group_settings")
        self.verticalLayout_6 = QVBoxLayout(self.group_settings)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(20, 9, 20, 20)
        self.label_link = QLabel(self.group_settings)
        self.label_link.setObjectName(u"label_link")
        self.label_link.setMinimumSize(QSize(0, 60))
        self.label_link.setMaximumSize(QSize(16777215, 60))
        self.label_link.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label_link.setWordWrap(True)

        self.verticalLayout_6.addWidget(self.label_link)

        self.frame_origin_detination = QFrame(self.group_settings)
        self.frame_origin_detination.setObjectName(u"frame_origin_detination")
        self.frame_origin_detination.setMinimumSize(QSize(0, 0))
        self.frame_origin_detination.setMaximumSize(QSize(16777215, 16777215))
        self.frame_origin_detination.setFrameShape(QFrame.StyledPanel)
        self.frame_origin_detination.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frame_origin_detination)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.formLayout.setHorizontalSpacing(10)
        self.formLayout.setVerticalSpacing(10)
        self.label_source = QLabel(self.frame_origin_detination)
        self.label_source.setObjectName(u"label_source")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_source)

        self.line_edit_source = QLineEdit(self.frame_origin_detination)
        self.line_edit_source.setObjectName(u"line_edit_source")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.line_edit_source.sizePolicy().hasHeightForWidth())
        self.line_edit_source.setSizePolicy(sizePolicy1)
        self.line_edit_source.setFrame(True)
        self.line_edit_source.setClearButtonEnabled(False)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.line_edit_source)

        self.label_destination = QLabel(self.frame_origin_detination)
        self.label_destination.setObjectName(u"label_destination")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_destination)

        self.line_edit_destination = QLineEdit(self.frame_origin_detination)
        self.line_edit_destination.setObjectName(u"line_edit_destination")
        sizePolicy1.setHeightForWidth(self.line_edit_destination.sizePolicy().hasHeightForWidth())
        self.line_edit_destination.setSizePolicy(sizePolicy1)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.line_edit_destination)


        self.verticalLayout_6.addWidget(self.frame_origin_detination, 0, Qt.AlignVCenter)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer)

        self.button_save = QPushButton(self.group_settings)
        self.button_save.setObjectName(u"button_save")

        self.verticalLayout_6.addWidget(self.button_save, 0, Qt.AlignHCenter)


        self.verticalLayout_2.addWidget(self.group_settings)

        app_pages.addWidget(self.page_settings)
        self.page_about = QWidget()
        self.page_about.setObjectName(u"page_about")
        self.horizontalLayout = QHBoxLayout(self.page_about)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_about = QFrame(self.page_about)
        self.frame_about.setObjectName(u"frame_about")
        self.frame_about.setFrameShape(QFrame.StyledPanel)
        self.frame_about.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_about)
        self.verticalLayout_7.setSpacing(20)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(20, -1, 20, -1)
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_3)

        self.label_tittle_about = QLabel(self.frame_about)
        self.label_tittle_about.setObjectName(u"label_tittle_about")
        self.label_tittle_about.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_tittle_about, 0, Qt.AlignVCenter)

        self.label_about = QLabel(self.frame_about)
        self.label_about.setObjectName(u"label_about")
        self.label_about.setTextFormat(Qt.AutoText)
        self.label_about.setScaledContents(False)
        self.label_about.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        self.label_about.setWordWrap(True)

        self.verticalLayout_7.addWidget(self.label_about, 0, Qt.AlignVCenter)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addWidget(self.frame_about)

        self.frame_author = QFrame(self.page_about)
        self.frame_author.setObjectName(u"frame_author")
        self.frame_author.setFrameShape(QFrame.StyledPanel)
        self.frame_author.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_author)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, -1, -1, 20)
        self.label_logo = QLabel(self.frame_author)
        self.label_logo.setObjectName(u"label_logo")
        self.label_logo.setMinimumSize(QSize(333, 290))
        self.label_logo.setMaximumSize(QSize(333, 290))
        self.label_logo.setPixmap(QPixmap(u"../images/logo/logo-and-text-white-3700px-3200px.png"))
        self.label_logo.setScaledContents(True)

        self.verticalLayout_3.addWidget(self.label_logo, 0, Qt.AlignHCenter)

        self.label_software = QLabel(self.frame_author)
        self.label_software.setObjectName(u"label_software")
        self.label_software.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_software, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.label_author = QLabel(self.frame_author)
        self.label_author.setObjectName(u"label_author")

        self.verticalLayout_3.addWidget(self.label_author, 0, Qt.AlignHCenter)


        self.horizontalLayout.addWidget(self.frame_author)

        app_pages.addWidget(self.page_about)

        self.retranslateUi(app_pages)

        app_pages.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(app_pages)
    # setupUi

    def retranslateUi(self, app_pages):
        app_pages.setWindowTitle(QCoreApplication.translate("app_pages", u"StackedWidget", None))
        self.group_update.setTitle(QCoreApplication.translate("app_pages", u"Op\u00e7\u00f5es de Atualiza\u00e7\u00e3o", None))
        self.label_update.setText(QCoreApplication.translate("app_pages", u"Esta op\u00e7\u00e3o busca os arquivos atualizados da rede industrial, o local pode ser ajustado na aba \"Configura\u00e7\u00f5es\". Selecione os itens que deseja atualizar.", None))
        self.check_tag.setText(QCoreApplication.translate("app_pages", u"TAG Database (.DB)", None))
        self.check_gfx.setText(QCoreApplication.translate("app_pages", u"Displays (.Gfx)", None))
        self.check_uptade_all.setText(QCoreApplication.translate("app_pages", u"Atualiza\u00e7\u00e3o completa", None))
        self.check_datalog.setText(QCoreApplication.translate("app_pages", u"Datalog (.mdf)", None))
        self.check_users.setText(QCoreApplication.translate("app_pages", u"Users (.act)", None))
        self.label_confirmation.setText(QCoreApplication.translate("app_pages", u"Os arquivos atuais da m\u00e1quina ser\u00e3o sobrescritos, deseja continuar?", None))
        self.button_confirm_uptade.setText(QCoreApplication.translate("app_pages", u"Sim", None))
        self.button_cancel_uptade.setText(QCoreApplication.translate("app_pages", u"N\u00e3o", None))
        self.button_uptade.setText(QCoreApplication.translate("app_pages", u"Atualizar", None))
        self.group_reboot.setTitle(QCoreApplication.translate("app_pages", u"Reiniciar", None))
        self.label_reboot.setText(QCoreApplication.translate("app_pages", u"Esta op\u00e7\u00e3o reinicia o supervis\u00f3rio RsView, fechando todos os servi\u00e7os e processos necess\u00e1rios para que o supervis\u00f3rio inicie corretamente.", None))
        self.button_reboot.setText(QCoreApplication.translate("app_pages", u"Reiniciar", None))
        self.group_settings.setTitle(QCoreApplication.translate("app_pages", u"Origem e desitino", None))
        self.label_link.setText(QCoreApplication.translate("app_pages", u"Informe o endere\u00e7o na rede do supervisorio atualizado, e o local para onde dever\u00e1 ser copiado. Ap\u00f3s salvar, o programa trabalhar\u00e1 nestes endere\u00e7os at\u00e9 a pr\u00f3xima interven\u00e7\u00e3o.", None))
        self.label_source.setText(QCoreApplication.translate("app_pages", u"Origem:", None))
        self.line_edit_source.setText(QCoreApplication.translate("app_pages", u"C:\\Users\\eduma\\OneDrive\\\u00c1rea de Trabalho\\ORIGEM", None))
        self.line_edit_source.setPlaceholderText(QCoreApplication.translate("app_pages", u"ex: \\\\10.31.3.166\\Supervisorio Caldeira atual", None))
        self.label_destination.setText(QCoreApplication.translate("app_pages", u"Destino:", None))
        self.line_edit_destination.setText(QCoreApplication.translate("app_pages", u"C:\\Users\\eduma\\OneDrive\\\u00c1rea de Trabalho\\DESTINO", None))
        self.line_edit_destination.setPlaceholderText(QCoreApplication.translate("app_pages", u"ex: C:\\Supervisorio Caldeira Atual", None))
        self.button_save.setText(QCoreApplication.translate("app_pages", u"Salvar", None))
        self.label_tittle_about.setText(QCoreApplication.translate("app_pages", u"Sobre", None))
        self.label_about.setText(QCoreApplication.translate("app_pages", u"Este software a visa auxiliar as atualiza\u00e7\u00f5es nos supervis\u00f3rios RsView da planta industrial, ap\u00f3s configurado ele fecha o supervis\u00f3rio aberto, busca o backup da rede, atualiza o projeto na m\u00e1quina e incia o supervis\u00f3rio novamente.", None))
        self.label_logo.setText("")
        self.label_software.setText(QCoreApplication.translate("app_pages", u"AtualizaSup - v1.0\n"
"Eduardo Marioti", None))
        self.label_author.setText("")
    # retranslateUi

