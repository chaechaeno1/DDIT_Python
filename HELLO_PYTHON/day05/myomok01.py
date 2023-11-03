import sys
from PyQt5 import uic, QtGui, QtCore 
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.Qt import QPushButton

form_class = uic.loadUiType("myomok01.ui")[0]

class WindowClass(QMainWindow, form_class): 
    def __init__(self):
        super().__init__()
        
        self.setupUi(self) # ui파일에서 불러온 폼 현재창에 설정
        
        self.flag = True; #오목알 색 바꾸기

        #qpushbutton을 생성한담에 for문으로 10*10만들기 
        for i in range(10): # 10x10 오목판
            for j in range(10): # 10x10 오목판
                pb = QPushButton('', self) #빈 텍스트 가지는 btn 생성. 각 셀을 의미.
                pb.setIcon(QtGui.QIcon('0.png')) #각 btn에 이미지 파일 설정
                pb.setIconSize(QtCore.QSize(40,40)) #아이콘 크기
                pb.setGeometry(QtCore.QRect(i*40,j*40,40,40)) #버튼 위치, 크기 결정
                pb.clicked.connect(self.myclick)
        self.show()
                
    def myclick(self):
        if self.flag : 
            self.sender().setIcon(QtGui.QIcon('1.png'))
        else :    
            self.sender().setIcon(QtGui.QIcon('2.png'))
        self.flag = not self.flag    

        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()