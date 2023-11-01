import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

form_class = uic.loadUiType("pyqt03.ui")[0]

class MainClass(QMainWindow, form_class):
    def __init__(self) :
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
        self.show()
        
    def myclick(self) :
        num1 = self.te1.toPlainText()
        num2 = self.te2.toPlainText()
        
        inum1 = int(num1)
        inum2 = int(num2)
                
        res = str(inum1-inum2)
        self.te3.setText(res)
        
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_()