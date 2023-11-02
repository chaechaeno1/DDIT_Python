import sys

from PyQt5 import uic, QtGui, QtCore

from PyQt5.Qt import QPixmap, QLabel, Qt, QPushButton, QMainWindow, QApplication

form_class = uic.loadUiType("myomok01.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self) # ui파일에서 불러온 폼 현재창에 설정

        #qpushbutton을 생성한담에 for문으로 10*10만들기 
        for i in range(10): # 10x10 오목판
            for j in range(10): # 10x10 오목판
                piece = QPushButton('', self) #빈 텍스트 가지는 btn 생성. 각 셀을 의미.
                piece.setIcon(QtGui.QIcon('0.png')) #각 btn에 이미지 파일 설정
                piece.setIconSize(QtCore.QSize(40,40)) #아이콘 크기
                piece.setGeometry(QtCore.QRect(i*40,j*40,40,40)) #버튼 위치, 크기 결정
        
        self.show()

        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()