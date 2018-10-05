import sys
from PyQt5.QtWidgets import (QWidget, QToolTip, QPushButton, QApplication, QInputDialog, QLineEdit)
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QIcon

class VRG(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 file dialogs - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('This is a <b>QWidget</b> widget')
        btn = QPushButton('Browse', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(50, 50)
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('VRG')
        
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = VRG()
    sys.exit(app.exec_())