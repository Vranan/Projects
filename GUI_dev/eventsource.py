#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial

In this example, we determine the event sender
object.

Author: Jan Bodnar
Website: zetcode.com
Last edited: August 2017
"""

import sys
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication,  QDialog, QToolTip, QPushButton, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont
from PyQt5 import QtCore
import xlrd
import xlwt

class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):

        btn1 = QPushButton("Button 1", self)
        btn1.move(30, 50)

        btn2 = QPushButton("Button 2", self)
        btn2.move(150, 50)

        btn1.clicked.connect(self.buttonClicked)
        btn2.clicked.connect(self.buttonClicked)

        self.statusBar()

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Event sender')
        self.show()


    #def buttonClicked(self):
    #    sender = self.sender()
    #    self.statusBar().showMessage(sender.text() + ' was pressed')

    def buttonClicked(self):
        sender = self.sender()
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        #fil     = QFileDialog.setNameFilter("Excel Sheets (*.csv *.xml *.xlsx);;Images (*.png *.jpg *.jpeg);; Python Files (*.py)")
        #print("options = %s" %(options))
        print("I am inside openFileNameDialog")
        fileName, NameFilter = QFileDialog.getOpenFileName(self,"Open the File", "","All Files (*);;Python Files (*.py)", options=options)
        #print("filename = %s" %fileName)
        if fileName:
            print("I Will Baby. I Will. %s" %fileName)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
