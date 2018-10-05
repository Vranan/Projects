import sys
import PyQt5.QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog, QToolTip, QPushButton, QWidget, QInputDialog, QLineEdit, QFileDialog, QComboBox
import PyQt5.QtGui
from PyQt5.QtGui import QIcon, QFont
from PyQt5 import QtCore
import xlrd
import xlwt
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile


class __VRG__(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn1 = QPushButton("Browse", self)
        btn1.move(30, 50)

        #btn2 = QPushButton("Button 2", self)
        #btn2.move(150, 50)

        btn1.clicked.connect(self.Browse)
        #btn2.clicked.connect(self.buttonClicked)

        self.statusBar()
        self.setGeometry(600, 600, 400, 400)
        self.setWindowTitle('__VRG__')
        self.show()

    def combolist(self,fileName):
        comboBox = PyQt5.QtWidgets.QComboBox(self)
        comboBox.addItem("Vayu")
        comboBox.addItem("Jal")
        comboBox.addItem("Agni")
        comboBox.addItem("Prithvi")
        comboBox.move(1, 1)

        df = pd.read_excel(fileName, sheetname='Sheet1')
        column_head = df.columns
        print("column headings \n")
        print(column_head)
        print(df['YEAR'])
        column_mean = df["YEAR"].mean()
        print("mean of the column = %d" %(column_mean))
        #for c in column_head:
        #    comboBox.addItems(self,c)


    def Browse(self):
        #sender = self.sender()
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, NameFilter = QFileDialog.getOpenFileName(self,"Open the File", "","All Files (*);;Python Files (*.py)", options=options)

        if fileName:
            self.combolist(fileName)
        #if fileName:
        #    print("I Will Baby. I Will. %s" %fileName)
        #    print(x1.sheet_names)



if __name__ == '__main__':
    #print("The name of the file = %s" %(sys.argv[0]))
    #print("The length of the file = %d" %(len(sys.argv)))
    #print("The arguments to the file = %s" %(str(sys.argv)))
    app = QApplication(sys.argv)
    ex = __VRG__()
    sys.exit(app.exec_())
