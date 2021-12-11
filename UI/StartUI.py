import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("StartUI.ui")[0]
form_error = uic.loadUiType("LoginError.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QDialog, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

class TestClass(QMainWindow, form_error) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 
    myLoginError = TestClass() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()
    myLoginError.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()
