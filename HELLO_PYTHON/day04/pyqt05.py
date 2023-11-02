from random import random
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


form_class = uic.loadUiType("pyqt05.ui")[0]

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
        
        if rnd > 0.5: com = "홀"
        else : com = "짝"
            
        if mine==com : res = "승리!"
        else : res = "패배.."  
        
        
        self.le_com.setText(com);
        self.le_result.setText(res);  
        
        
         
      
    

if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_()