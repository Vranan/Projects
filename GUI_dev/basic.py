import sys
from PyQt5 import QtGui, QtCore

def window():
    app = QtGui.QApplication(sys.argv)
    w = QtGui.QWidget()
    b = QtGui.QLabel(w)
    b.setText("I Will Do What I Love More!! ")
    w.setGeometry(100,100,200,200)
    b.move(50,20)
    w.setWindowTitle("VRG")
    w.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    window()
