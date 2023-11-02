import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from IPython.lib.tests.test_pretty import SB


form_class = uic.loadUiType("pyqt06.ui")[0]

class MainClass(QMainWindow, form_class):
    def __init__(self) :
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
        self.show()
        
        #self가 붙으면 전역변수
    def myclick(self) :
        dan = self.sb.value();
        # print(type(dan))
        
        arr = range(1,10);
        
        code = "";
        for i in arr:
            code += "{} * {} = {}".format(dan,i,i*dan)
            code += "\n"
        self.te.setText(code)
                  

if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_()