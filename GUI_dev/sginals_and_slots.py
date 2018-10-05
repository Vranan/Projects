from PyQt5.QtWidgets import (QApplication, QComboBox, QDialog,
        QDialogButtonBox, QFormLayout, QFileDialog, QGridLayout, QGroupBox, QHBoxLayout,
        QInputDialog, QLabel, QLineEdit, QMenu, QMenuBar, QPushButton, QSpinBox, QTextEdit,
        QVBoxLayout, QToolTip, QWidget)

from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont
import xlrd
import xlwt
import sys

class Dialog(QDialog):

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        #fil     = QFileDialog.setNameFilter("Excel Sheets (*.csv *.xml *.xlsx);;Images (*.png *.jpg *.jpeg);; Python Files (*.py)")
        #print("options = %s" %(options))
        fileName, NameFilter = QFileDialog.getOpenFileName(self,"Open the File", "","All Files (*);;Python Files (*.py)", options=options)
        #rint("filename = %s" %fileName)
        if fileName:
            print("I Will Baby. I Will. %s" %fileName)
            #workbook = xlrd.open_workbook(fileName)
            #worksheet = workbook.sheet_by_name('Sheet1')    or
            #worksheet = workbook.sheet_by_name(0)

    def func(self):
        print("I have clicked the button")

    def __init__(self):
        super(Dialog, self).__init__()

        button=QPushButton("Click")
        button.clicked.connect(self.func())

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(button)

        self.setLayout(mainLayout)
        self.setWindowTitle("Button Example - pythonspot.com")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = Dialog()
sys.exit(dialog.exec_())
