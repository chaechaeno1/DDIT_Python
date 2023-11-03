import sys
from PyQt5 import uic, QtGui, QtCore 
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.Qt import QPushButton
from _ast import If
from astropy.time.utils import split

form_class = uic.loadUiType("myomok02.ui")[0]

class WindowClass(QMainWindow, form_class): 
    def __init__(self):
        super().__init__()
        
        #5개 맞추기 위해 arr 툴 만들었음
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
        #배열안에 배열 넣으면 2차원 구조가 됨
        self.pb2D = []
        self.setupUi(self) # ui파일에서 불러온 폼 현재창에 설정

        self.flagWb = True; #오목알 색 바꾸기

        #qpushbutton을 생성한담에 for문으로 10*10만들기 
        for i in range(10): 
            line = []
            for j in range(10): # 10x10 오목판
                pb = QPushButton('', self) #빈 텍스트 가지는 btn 생성. 각 셀을 의미.
                pb.setToolTip("{},{}".format(i,j)) 
                pb.setIcon(QtGui.QIcon('0.png')) #각 btn에 이미지 파일 설정
                pb.setIconSize(QtCore.QSize(40,40)) #아이콘 크기
                pb.setGeometry(QtCore.QRect(j*40,i*40,40,40)) #배열의 기준으로 i,j 순서 바꿔줌
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
    
    def getUP(self,i,j,stone):        
        cnt = 0
        try:
            while True:
                    i-=1  
                    if i < 0 :
                        return cnt                  
                    if self.arr2D[i][j] == stone:
                        cnt+=1           
                    else :
                        return cnt
        except:
            return cnt    
                
    def getDW(self,i,j,stone):        
        cnt = 0
        
        try:
            while True:
                    i+=1  
                    if i < 0 :
                        return cnt      
                                
                    if self.arr2D[i][j] == stone:
                        cnt+=1           
                    else :
                        return cnt
        except:
            return cnt 
                  
    def getLE(self,i,j,stone):        
        cnt = 0
        
        try:
            while True:
                    j-=1  
                    if i < 0 :
                        return cnt      
                                
                    if self.arr2D[i][j] == stone:
                        cnt+=1           
                    else :
                        return cnt
        except:
            return cnt   
                
    def getRI(self,i,j,stone):        
        cnt = 0
        
        try:
            while True:
                    j+=1  
                    if i < 0 :
                        return cnt      
                                
                    if self.arr2D[i][j] == stone:
                        cnt+=1           
                    else :
                        return cnt
        except:
            return cnt    
               
    def getUL(self,i,j,stone):        
        cnt = 0
        
        try:
            while True:
                    i-=1
                    j-=1  
                    if i < 0 :
                        return cnt      
                                
                    if self.arr2D[i][j] == stone:
                        cnt+=1           
                    else :
                        return cnt
        except:
            return cnt           
            
            
            
            
            
            
    def myclick(self):

        str_ij = self.sender().toolTip()
        arr_ij = str_ij.split(",")
        str_i = arr_ij[0]
        str_j = arr_ij[1]
        i = int(str_i)
        j = int(str_j)
        
        #돌이 놓여진 곳에 중복 클릭 되지않도록
        if self.arr2D[i][j] > 0 :
            return
        
        #오목알 색 바꾸기
        stone = -1
        if self.flagWb :
            self.arr2D[i][j]=1 
            stone = 1 
        else : 
            self.arr2D[i][j]=2
            stone = 2
        
                
        up = self.getUP(i,j,stone)
        print("up",up)
        
        dw = self.getDW(i,j,stone)
        print("dw",dw)
        
        le = self.getLE(i,j,stone)
        print("le",le)
        
        ri = self.getRI(i,j,stone)
        print("ri",ri)
        
        ul = self.getUL(i,j,stone)
        print("ul",ul)

        # ur = self.getUR(i,j,stone)
        # print("ur",ur)
        #
        # dl = self.getDL(i,j,stone)
        # print("dl",dl)
        #
        # dr = self.getDR(i,j,stone)
        # print("dr",dr)
        
        

        self.myrender()
        
        #순서 바꾸기    
        self.flagWb = not self.flagWb      
            


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()