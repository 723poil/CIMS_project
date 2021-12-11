import sys, os
sys.path.append(os.path.dirname( os.path.abspath( os.path.dirname(__file__) ) ))

import login_function
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtWidgets


#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
SignInWindow = uic.loadUiType("UI\SignIn.ui")[0]
SignUpWindow = uic.loadUiType("UI\SignUp.ui")[0]

#widget = QtWidgets.QStackedWidget()
#widgetindex = 0
#화면을 띄우는데 사용되는 Class 선언
class SignInClass(QMainWindow, SignInWindow) :

    email = ''
    password = ''

    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.Signin.clicked.connect(self.ClickedOkButton)

    def ClickedOkButton(self):
        self.email = self.Email.text()
        self.password = self.Password.text()

        if(login_function.sign_in(self.email,self.password) == -1):
             QMessageBox.about(self,'SignIn Fail','아이디나 비밀번호가 틀렸습니다.')


class SignUpClass(QDialog, SignUpWindow) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.OkButton.clicked.connect(self.ClickedOkButton)
        self.CancleButton.clicked.connect(self.ClickedCancleButton)
        
    def ClickedOkButton(self):
        email = self.EmailLine.text()
        password = self.PasswordLine.text()
        name = self.NameLine.text()
        birth = self.BirthLine.text()
        address = self.AddressLine.text()
        job = self.JobLine.text()
        RRN = self.RRNLine.text()
        phone_number = self.PhoneLine.text()

        registration_info = {
            'Email' : email,
            'Password' : password,
            'Name' : name,
            'Birth' : birth,
            'Address' : address,
            'Job' : job,
            'Phone number' : phone_number
        }
        login_function.sign_up(registration_info)

    def ClickedCancleButton(self):   
        self.close()


if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    signinwindow = SignInClass() 
    signupwindow = SignUpClass()

    #프로그램 화면을 보여주는 코드
    signinwindow.show()
    signupwindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()
