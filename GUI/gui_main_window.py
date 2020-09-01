#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/19 20:05
# @Author  : Geniuswei
# @Email   : iamgeniuswei@sina.com
# @File    : gui_main_window.py
# @Desc    :
from PySide2.QtWidgets import QApplication,QMainWindow
from .main_window import *

class GUIMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(GUIMainWindow, self).__init__(parent)
        self.setupUi(self)