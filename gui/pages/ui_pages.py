# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pagesMmzNeV.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qt_core import *

class Ui_app_pages(object):
    def setupUi(self, app_pages):
        if not app_pages.objectName():
            app_pages.setObjectName(u"app_pages")
        app_pages.resize(400, 300)
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.verticalLayout = QVBoxLayout(self.page_1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_3 = QLabel(self.page_1)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_3)

        app_pages.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_2 = QVBoxLayout(self.page_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.page_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        app_pages.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_3 = QVBoxLayout(self.page_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.page_3)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)

        app_pages.addWidget(self.page_3)

        self.retranslateUi(app_pages)

        QMetaObject.connectSlotsByName(app_pages)
    # setupUi

    def retranslateUi(self, app_pages):
        app_pages.setWindowTitle(QCoreApplication.translate("app_pages", u"StackedWidget", None))
        self.label_3.setText(QCoreApplication.translate("app_pages", u"P\u00e1gina 1", None))
        self.label_2.setText(QCoreApplication.translate("app_pages", u"P\u00e1gina 2", None))
        self.label.setText(QCoreApplication.translate("app_pages", u"P\u00e1gina 3", None))
    # retranslateUi

