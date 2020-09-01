# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionCNKI_XLS_Format = QAction(MainWindow)
        self.actionCNKI_XLS_Format.setObjectName(u"actionCNKI_XLS_Format")
        self.action = QAction(MainWindow)
        self.action.setObjectName(u"action")
        self.action_2 = QAction(MainWindow)
        self.action_2.setObjectName(u"action_2")
        self.action_3 = QAction(MainWindow)
        self.action_3.setObjectName(u"action_3")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 23))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menu.addAction(self.action)
        self.menu.addAction(self.action_2)
        self.menu.addAction(self.action_3)
        self.menu_2.addAction(self.actionCNKI_XLS_Format)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u6587\u732e\u8ba1\u91cf\u53ef\u89c6\u5316\u7cfb\u7edf", None))
        self.actionCNKI_XLS_Format.setText(QCoreApplication.translate("MainWindow", u"CNKI-XLS Format", None))
        self.action.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u9879\u76ee", None))
        self.action_2.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u9879\u76ee", None))
        self.action_3.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u9879\u76ee", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u9879\u76ee", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u6807\u51c6\u5316", None))
    # retranslateUi

