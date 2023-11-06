import sys
from PyQt5 import uic, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.Qt import QPushButton, QMessageBox
from _ast import If

form_class = uic.loadUiType("pyomok02.ui")[0]

class MainClass(QMainWindow, form_class):
    def __init__(self) :
        QMainWindow.__init__(self)
        self.flagWb = True
        self.flagOver = False
        self.arr2D=[
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0],
            [0,0,0,0,0, 0,0,0,0,0]
        ]
        self.pb2D = []
        self.setupUi(self)
        
        for i in range(10):
            line = []
            for j in range(10):
                pb = QPushButton("", self)
                pb.setToolTip("{},{}".format(i,j))
                pb.setIcon(QtGui.QIcon('0.png'))
                pb.setIconSize(QtCore.QSize(40,40))
                pb.setGeometry(QtCore.QRect(j*40, i*40, 40, 40))
                pb.clicked.connect(self.myclick)
                line.append(pb)
            self.pb2D.append(line)
        
        
        self.show()
        self.myrender()
        
    def myrender(self):
        for i in range(10):
            for j in range(10):
                if self.arr2D[i][j]==0:
                    self.pb2D[i][j].setIcon(QtGui.QIcon('0.png'))
                if self.arr2D[i][j]==1:
                    self.pb2D[i][j].setIcon(QtGui.QIcon('1.png'))
                if self.arr2D[i][j]==2:
                    self.pb2D[i][j].setIcon(QtGui.QIcon('2.png'))
                    
                    
    def getRI(self,i,j,stone):
        cnt = 0 
        try:
            while True:
                j+=1
                if i <0 :
                    return cnt
                if j <0 :
                    return cnt
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt        
                    
    def getLE(self,i,j,stone):
        cnt = 0 
        try:
            while True:
                j-=1
                if i <0 :
                    return cnt
                if j <0 :
                    return cnt
                
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
    
    def getUP(self,i,j,stone):
        cnt = 0 
        try:
            while True:
                i-=1
                if i <0 :
                    return cnt
                if j <0 :
                    return cnt
                
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt

    def getDW(self,i,j,stone):
        cnt = 0 
        try:
            while True:
                i+=1
                if i <0 :
                    return cnt
                if j <0 :
                    return cnt
                
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
        
    def getUL(self,i,j,stone):
        cnt = 0 
        try:
            while True:
                i-=1
                j-=1
                if i <0 :
                    return cnt
                if j <0 :
                    return cnt
                
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
        
    def getUR(self,i,j,stone):
        cnt = 0 
        try:
            while True:
                i-=1
                j+=1
                if i <0 :
                    return cnt
                if j <0 :
                    return cnt
                
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
        
    def getDL(self,i,j,stone):
        cnt = 0 
        try:
            while True:
                i+=1
                j-=1
                if i <0 :
                    return cnt
                if j <0 :
                    return cnt
                
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
        
    def getDR(self,i,j,stone):
        cnt = 0 
        try:
            while True:
                i+=1
                j+=1
                if i <0 :
                    return cnt
                if j <0 :
                    return cnt
                
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt
                
    def myclick(self):
        if self.flagOver:
            return
        
        str_ij = self.sender().toolTip()
        arr_ij = str_ij.split(",")
        str_i = arr_ij[0]
        str_j = arr_ij[1]
        i = int(str_i)
        j = int(str_j)
        
        if self.arr2D[i][j]>0:
            return
        
        stone = -1
        if self.flagWb:
            self.arr2D[i][j]=1
            stone = 1
        else:
            self.arr2D[i][j]=2
            stone = 2
        
        up = self.getUP(i,j,stone)
        dw = self.getDW(i,j,stone)
        le = self.getLE(i,j,stone)
        ri = self.getRI(i,j,stone)
        
        ur = self.getUR(i,j,stone)
        ul = self.getUL(i,j,stone)
        dr = self.getDR(i,j,stone)
        dl = self.getDL(i,j,stone)
        
        d1 = up + dw + 1
        d2 = ur + dl + 1
        d3 = le + ri + 1
        d4 = ul + dr + 1
        
        self.myrender()
        
        if d1==5 or d2==5 or d3==5 or d4==5:
            QMessageBox.about(self,'오목','GAME OVER')
            self.flagOver = True

        
        self.flagWb = not self.flagWb
        

        

        
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_()
    
    
    
    
    
    
    
    