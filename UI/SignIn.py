import sys, os
sys.path.append(os.path.dirname( os.path.abspath( os.path.dirname(__file__) ) ))

import login_function
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtWidgets

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
SignInWindow = uic.loadUiType("UI\\SignIn.ui")[0]
SignUpWindow = uic.loadUiType("UI\\SignUp.ui")[0]
UserMenuWindow = uic.loadUiType("UI\\UserMenu.ui")[0]
AdminMenuWindow = uic.loadUiType("UI\\AdminMenu.ui")[0]
TotalInfoWindow = uic.loadUiType("UI\\TotalInfoWindow.ui")[0]
form_reportlist = uic.loadUiType("UI/Report_List.ui")[0]
form_reportcheck = uic.loadUiType("UI\\Reportcheck.ui")[0]
form_report = uic.loadUiType("UI\\Report.ui")[0]
form_viewinformation = uic.loadUiType("UI\\ViewInformation.ui")[0]
form_impactedlist = uic.loadUiType("UI\\Impacted_List.ui")[0]
form_visitplacelist = uic.loadUiType("UI\\VisitPlace_List.ui")[0]
form_alarmlist = uic.loadUiType("UI\\Alarm_List.ui")[0]

class TotalInfoClass(QMainWindow, TotalInfoWindow) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.Back.clicked.connect(self.ClickedBackButton)
        self.alarmbutton.clicked.connect(self.AlarmButtonFunction)
        self.listWidget.itemDoubleClicked.connect(self.ViewInfoOpen)

    def ClickedBackButton(self):    
        widget.setFixedHeight(615)
        widget.setFixedWidth(800)
        widget.setCurrentIndex(widget.currentIndex()-2)

    def AlarmButtonFunction(self) :
        myalarm.show()

        #더블 클릭 했을 때 함수
    def ViewInfoOpen(self) :
        myViewInformation.show()

class AdminTotalInfoClass(QMainWindow, TotalInfoWindow) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.Back.clicked.connect(self.ClickedBackButton)
        self.alarmbutton.clicked.connect(self.AlarmButtonFunction)
        self.alarmbutton.setText("설정")

    def ClickedBackButton(self):    
        widget.setFixedHeight(615)
        widget.setFixedWidth(800)
        widget.setCurrentIndex(widget.currentIndex()-2)

    def AlarmButtonFunction(self) :
        print()


class UserMenuClass(QMainWindow, UserMenuWindow) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.DisplayInfo.clicked.connect(self.ClickedDisplayInfoButton)
        self.SearchVisitPlace.clicked.connect(self.ClickedSearchVisitPlaceButton)
        self.SearchImpactedPlace.clicked.connect(self.ClickedSearchImpactedPlaceButton)

    def ClickedDisplayInfoButton(self):
        widget.setFixedHeight(914)
        widget.setFixedWidth(964)
        widget.setCurrentIndex(widget.currentIndex()+2)
        
    def ClickedSearchVisitPlaceButton(self):    
        myVisitPlaceList.show()
    def ClickedSearchImpactedPlaceButton(self):
        myImpactedList.show()

class AdminMenuClass(QMainWindow, AdminMenuWindow) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        self.ReportList.clicked.connect(self.ReportListFunction)
        self.ModificationBoard.clicked.connect(self.ModificationBoardFunction)
        # 버튼 클릭 시 함수
    def ReportListFunction(self) :
        myReportList.show()

    def ModificationBoardFunction(self):
        widget.setFixedHeight(914)
        widget.setFixedWidth(964)
        widget.setCurrentIndex(widget.currentIndex()+2)


#Sign in class 선언
class SignInClass(QMainWindow, SignInWindow) :

    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.Signin.clicked.connect(self.ClickedSigninButton)
        self.Signup.clicked.connect(self.ClickedSignUpButton)

    def ClickedSigninButton(self):
        email = self.Email.text()
        password = self.Password.text()

        sign_info = {
            'Email' : email,
            'Password' : password,
        }
        #로그인 기능
        #login = login_function.sign_in(sign_info['Email'],sign_info['Password'])
        #if(login == -1):
        #    QMessageBox.about(self,'SignIn Fail','아이디나 비밀번호가 틀렸습니다.')
        #elif(login == 1):
        #widget.setFixedHeight(615)
        #widget.setFixedWidth(800)
        #widget.setCurrentIndex(widget.currentIndex()+1)
        #elif(login == 2):
        widget.setFixedHeight(615)
        widget.setFixedWidth(800)
        widget.setCurrentIndex(widget.currentIndex()+2)

    def ClickedSignUpButton(self): 
        SignUpClass(self)  
        
#Sign up class 선언
class SignUpClass(QDialog, SignUpWindow) :
    def __init__(self,parent):
        super().__init__(parent)
        self.setupUi(self)
        self.show()
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


class ViewInformation(QMainWindow, form_viewinformation) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        
        #정보 열람의 버튼 함수
        self.ReportButton.clicked.connect(self.ReportButtonFunction)
        
        #Report버튼 클릭 시 작동 함수
    def ReportButtonFunction(self) :
        myReport.show()
        
class Report(QDialog, form_report) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)      
        
        # 신고 기능의 버튼 함수
        self.CancleButton.clicked.connect(self.CancleFunction)
        
        #cancle 클릭 시 실행 함수
    def CancleFunction(self) :
        self.close()
        
class VisitPlaceList(QDialog, form_visitplacelist) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)        

        # 검색 버튼 함수
        self.SearchButton.clicked.connect(self.SearchButtonFunction)
        
        #search 버튼 클릭 시 작동 함수
    def SearchButtonFunction(self) :
        self.close()
        myVisitPlaceList.show()
        
class ImpactedList(QDialog, form_impactedlist) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)  
        
        # 검색 버튼 함수
        self.SearchButton.clicked.connect(self.SearchButtonFunction)
        
        #search 버튼 클릭 시 작동 함수
    def SearchButtonFunction(self) :
        self.close()
        myImpactedList.show()
        
class ReportList(QDialog, form_reportlist) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)  
        
        #리폿리스트 안에 항목을 더블 클릭시 
        self.listWidget.itemDoubleClicked.connect(self.ReportCheckOpen)

        #더블 클릭 했을 때 함수
    def ReportCheckOpen(self) :
        myReportCheck.show()

class ReportCheck(QDialog, form_reportcheck) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)  
        
        # 신고체크 기능의 버튼 함수
        self.CancleButton.clicked.connect(self.CancleFunction)
        
        #cancle 클릭 시 실행 함수
    def CancleFunction(self) :
        self.close()

class AlarmList(QDialog, form_alarmlist) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)  
        
        #리폿리스트 안에 항목을 더블 클릭시 
        self.listWidget.itemDoubleClicked.connect(self.ReportCheckOpen)

        #더블 클릭 했을 때 함수
    def ReportCheckOpen(self) :
        myReportCheck.show()        

if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    widget = QtWidgets.QStackedWidget()

    #WindowClass의 인스턴스 생성
    signinwindow = SignInClass() 
    userMenuWindow = UserMenuClass() 
    adminMenuWindow = AdminMenuClass()
    totalInfoWindow = TotalInfoClass() 
    AdmintotalInfoWindow = AdminTotalInfoClass() 

    myViewInformation = ViewInformation()
    myReport = Report()
    myVisitPlaceList = VisitPlaceList()
    myImpactedList = ImpactedList()
    myReportList = ReportList()
    myReportCheck = ReportCheck()
    myalarm = AlarmList()

    #화면 전환용 위젯추가
    widget.addWidget(signinwindow)
    widget.addWidget(userMenuWindow)
    widget.addWidget(adminMenuWindow)
    widget.addWidget(totalInfoWindow)
    widget.addWidget(AdmintotalInfoWindow)

    #프로그램 화면을 보여주는 코드
    widget.setFixedHeight(720)
    widget.setFixedWidth(1280)
    widget.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()
