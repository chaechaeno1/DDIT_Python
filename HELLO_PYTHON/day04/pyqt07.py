import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import random


form_class = uic.loadUiType("pyqt07.ui")[0]

class MainClass(QMainWindow, form_class):
    def __init__(self) :
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
        self.le_mine.returnPressed.connect(self.myclick)
        self.show()
        
        #self가 붙으면 전역변수
    def myclick(self) :
        mine = self.le_mine.text();
        com = "";
        res = "";
        
        rnd = random();
        
        if rnd > 0.66 : com = "가위"
        elif rnd < 0.33 : com = "바위"
        else : com = "보"
        
        if mine==com : 
            res = "비김!"
        elif (mine=="가위" and com=="보") or (mine=="바위" and com=="가위") or (mine=="보" and com=="바위"):
            res = "승리!"
        else : 
            res = "패배..."
        
        self.le_com.setText(com);
        self.le_result.setText(res); 
        
        
 

if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_()