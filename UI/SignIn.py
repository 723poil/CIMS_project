import sys, os
sys.path.append(os.path.dirname( os.path.abspath( os.path.dirname(__file__) ) ))

import login_function
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtWidgets
import db as dbfile

userid = ''

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
SignInWindow = uic.loadUiType("C:/CIMS_PROJECT/UI/ui_folder/SignIn.ui")[0]
SignUpWindow = uic.loadUiType("C:/CIMS_PROJECT/UI/ui_folder/SignUp.ui")[0]
UserMenuWindow = uic.loadUiType("C:/CIMS_PROJECT/UI/ui_folder/UserMenu.ui")[0]
AdminMenuWindow = uic.loadUiType("C:/CIMS_PROJECT/UI/ui_folder/AdminMenu.ui")[0]
TotalInfoWindow = uic.loadUiType("C:/CIMS_PROJECT/UI/ui_folder/TotalInfoWindow.ui")[0]
form_reportlist = uic.loadUiType("C:/CIMS_PROJECT/UI/ui_folder/Report_List.ui")[0]
form_reportcheck = uic.loadUiType("C:/CIMS_PROJECT/UI/ui_folder/Reportcheck.ui")[0]
form_report = uic.loadUiType("C:/CIMS_PROJECT/UI/ui_folder/Report.ui")[0]
form_viewinformation = uic.loadUiType("C:/CIMS_PROJECT/UI/ui_folder/ViewInformation.ui")[0]
form_impactedlist = uic.loadUiType("C:/CIMS_PROJECT/UI/ui_folder/Impacted_List.ui")[0]
form_visitplacelist = uic.loadUiType("C:/CIMS_PROJECT/UI/ui_folder/VisitPlace_List.ui")[0]
form_alarmlist = uic.loadUiType("C:/CIMS_PROJECT/UI/ui_folder/Alarm_List.ui")[0]

class TotalInfoClass(QMainWindow, TotalInfoWindow) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.Back.clicked.connect(self.ClickedBackButton)
        self.alarmbutton.clicked.connect(self.AlarmButtonFunction)
        self.VaccineInfo.clicked.connect(self.VaccineInfoButtonFunction)
        self.CorronaInfo.clicked.connect(self.CorronaInfoButtonFunction)
        self.EventInfo.clicked.connect(self.EventInfoButtonFunction)
        self.Infected_personInfo.clicked.connect(self.Infected_personInfoButtonFunction)

        self.corona = dbfile.get_corona()
        self.quarantine_measures = dbfile.get_distancing()
        self.vaccine = dbfile.get_vaccine()
        self.coevent = dbfile.get_event()
        self.Ip = dbfile.get_Infected_person()
        self.news = dbfile.get_news()
        self.qm = dbfile.get_distancing()

    def ClickedBackButton(self):    
        widget.setFixedHeight(615)
        widget.setFixedWidth(800)
        widget.setCurrentIndex(widget.currentIndex()-2)

    def AlarmButtonFunction(self) :
        myalarm.show()
        
    def VaccineInfoButtonFunction(self) :
        self.MainMenuList.clear()
        self.smallMenuList.clear()
        self.smallMenuList.addItem("모더나")
        self.smallMenuList.itemClicked.connect(self.SetMainList)

    def CorronaInfoButtonFunction(self) : 
        self.MainMenuList.clear()
        self.smallMenuList.clear()
        self.smallMenuList.addItem("정의")
        self.smallMenuList.addItem("증상")
        self.smallMenuList.addItem("검사 방법")
        self.smallMenuList.addItem("자가 진단")
        self.smallMenuList.addItem("행동 수칙") 
        self.smallMenuList.addItem("방역 대책")
        self.smallMenuList.addItem("코로나 관련 뉴스")

    def EventInfoButtonFunction(self) :
        self.MainMenuList.clear()
        self.smallMenuList.clear()
        self.smallMenuList.addItem("인천광역시")

    def Infected_personInfoButtonFunction(self) :
        self.MainMenuList.clear()
        self.smallMenuList.clear()
        self.smallMenuList.addItem("확진자 수")

    def SetMainList(self) :
        select = self.smallMenuList.currentItem().text()
        self.MainMenuList.clear()

        if select == "모더나" :
            self.MainMenuList.addItem(
                "제조사 : " + self.vaccine['Moderna'].company + '\n\n' +
                "예약 방법 : " + self.vaccine['Moderna'].how_apply + '\n\n' +
                "필요 접종량 : " + self.vaccine['Moderna'].inoculation_capacity + '\n\n' +
                "접종 간격 : " + self.vaccine['Moderna'].inoculation_gap + '\n\n' +
                "접종자 수 : " + self.vaccine['Moderna'].inoculation_person_num + '\n\n' +
                "접종률 : " + self.vaccine['Moderna'].inoculation_rate + '\n\n' +
                "백신 이름 : " + self.vaccine['Moderna'].name + '\n\n' +
                "예방 효과 : " + self.vaccine['Moderna'].preventive_effects + '\n\n' +
                "필요 접종 횟수 : " + self.vaccine['Moderna'].required_inoculations + '\n\n' +
                "부작용 사례 : " + self.vaccine['Moderna'].side_effect_ex + '\n\n'
            )
        elif select == "정의":
            self.MainMenuList.addItem(self.corona.definition)
        elif select == "증상":
            self.MainMenuList.addItem(self.corona.symptom)
        elif select == "검사 방법":
            self.MainMenuList.addItem(self.corona.how_test)
        elif select == "자가 진단":
            self.MainMenuList.addItem(self.corona.self_test)
        elif select == "행동 수칙":
            self.MainMenuList.addItem(self.corona.action_tip)
        elif select == "방역 대책":
            self.MainMenuList.addItem("대구\n\n")
            self.MainMenuList.addItem(self.qm.Daegu['restrictions'] + '\n\n' +
            "-----------------------------------------------------------------------------------------------------------------------"
            )
        elif select == "인천광역시":
            for i in range(0, len(self.coevent['Incheon'])):
                self.MainMenuList.addItem(
                    "지역 : " + self.coevent['Incheon'][i].area + '\n\n' +
                    "카테고리 : " + self.coevent['Incheon'][i].category + '\n\n' +
                    "행사 이름 : " + self.coevent['Incheon'][i].name + '\n\n' +
                    "내용 : " + self.coevent['Incheon'][i].information + '\n\n' +
                    "-----------------------------------------------------------------------------------------------------------------------"
                )
        elif select == "확진자 수":
            for i in self.Ip:
                self.MainMenuList.addItem(
                    "일자 : " + i + '\n\n' +
                    "누적 확진자 수 : " + self.Ip[i].accumation + '\n\n' +
                    "일일 확진자 수 : " + self.Ip[i].day + '\n\n' +
                    "일일 사망 수 : " + self.Ip[i].death + '\n\n' +
                    "완치 수 : " + self.Ip[i].complete + '\n\n' +
                    "-----------------------------------------------------------------------------------------------------------------------"
                )
        elif select == "코로나 관련 뉴스":
            for i in self.news:
                self.MainMenuList.addItem(
                    "제목 : " + i.title + '\n\n' +
                    "기자 : " + i.repoter + '\n\n' +
                    "일자 : " + i.date + '\n\n' +
                    "매체 : " + i.media + '\n\n' +
                    "내용 : " + i.content + '\n\n' +
                    "출처 : " + i.source + '\n\n' +
                    "-----------------------------------------------------------------------------------------------------------------------"
                )

    def ViewInfo(self) :
        myViewInformation.setup(self)
        myViewInformation.show()
        

    def getMainMenuListClickedInfo(self) :
        return self.MainMenuList.currentItem().text()
class AdminTotalInfoClass(QMainWindow, TotalInfoWindow) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.Back.clicked.connect(self.ClickedBackButton)
        self.alarmbutton.clicked.connect(self.AlarmButtonFunction)
        self.VaccineInfo.clicked.connect(self.VaccineInfoButtonFunction)
        self.CorronaInfo.clicked.connect(self.CorronaInfoButtonFunction)
        self.EventInfo.clicked.connect(self.EventInfoButtonFunction)
        self.Infected_personInfo.clicked.connect(self.Infected_personInfoButtonFunction)
        self.alarmbutton.setText("설정")

    def ClickedBackButton(self):    
        widget.setFixedHeight(615)
        widget.setFixedWidth(800)
        widget.setCurrentIndex(widget.currentIndex()-2)

    def AlarmButtonFunction(self) :
        myalarm.show()
        
    def VaccineInfoButtonFunction(self) :
        self.MainMenuList.clear()
        self.smallMenuList.clear()
        self.smallMenuList.addItem("모더나")
        self.smallMenuList.itemClicked.connect(self.SetMainList)

    def CorronaInfoButtonFunction(self) : 
        self.MainMenuList.clear()
        self.smallMenuList.clear()
        self.smallMenuList.addItem("정의")
        self.smallMenuList.addItem("증상")
        self.smallMenuList.addItem("검사 방법")
        self.smallMenuList.addItem("자가 진단")
        self.smallMenuList.addItem("행동 수칙") 
        self.smallMenuList.addItem("방역 대책")

    def EventInfoButtonFunction(self) :
        self.MainMenuList.clear()
        self.smallMenuList.clear()
        self.smallMenuList.addItem("인천광역시")

    def Infected_personInfoButtonFunction(self) :
        self.MainMenuList.clear()
        self.smallMenuList.clear()
        self.smallMenuList.addItem("확진자 수")

    def SetMainList(self) :
        select = self.smallMenuList.currentItem().text()
        self.MainMenuList.clear()

        if select == "모더나" :
            self.MainMenuList.addItem(
                "제조사 : " + self.vaccine['Moderna'].company + '\n\n' +
                "예약 방법 : " + self.vaccine['Moderna'].how_apply + '\n\n' +
                "필요 접종량 : " + self.vaccine['Moderna'].inoculation_capacity + '\n\n' +
                "접종 간격 : " + self.vaccine['Moderna'].inoculation_gap + '\n\n' +
                "접종자 수 : " + self.vaccine['Moderna'].inoculation_person_num + '\n\n' +
                "접종률 : " + self.vaccine['Moderna'].inoculation_rate + '\n\n' +
                "백신 이름 : " + self.vaccine['Moderna'].name + '\n\n' +
                "예방 효과 : " + self.vaccine['Moderna'].preventive_effects + '\n\n' +
                "필요 접종 횟수 : " + self.vaccine['Moderna'].required_inoculations + '\n\n' +
                "부작용 사례 : " + self.vaccine['Moderna'].side_effect_ex + '\n\n'
            )
        elif select == "정의":
            self.MainMenuList.addItem(self.corona.definition)
        elif select == "증상":
            self.MainMenuList.addItem(self.corona.symptom)
        elif select == "검사 방법":
            self.MainMenuList.addItem(self.corona.how_test)
        elif select == "자가 진단":
            self.MainMenuList.addItem(self.corona.self_test)
        elif select == "행동 수칙":
            self.MainMenuList.addItem(self.corona.action_tip)
        elif select == "방역 대책":
            self.MainMenuList.addItem("대구")
        elif select == "인천광역시":
            for i in range(0, len(self.coevent['Incheon'])):
                self.MainMenuList.addItem(
                    "지역 : " + self.coevent['Incheon'][i].area + '\n\n' +
                    "카테고리 : " + self.coevent['Incheon'][i].category + '\n\n' +
                    "행사 이름 : " + self.coevent['Incheon'][i].name + '\n\n' +
                    "내용 : " + self.coevent['Incheon'][i].information + '\n\n' +
                    "-----------------------------------------------------------------------------------------------------------------------"
                )
        elif select == "확진자 수":
            for i in self.Ip:
                self.MainMenuList.addItem(
                    "일자 : " + i + '\n\n' +
                    "누적 확진자 수 : " + self.Ip[i].accumation + '\n\n' +
                    "일일 확진자 수 : " + self.Ip[i].day + '\n\n' +
                    "일일 사망 수 : " + self.Ip[i].death + '\n\n' +
                    "완치 수 : " + self.Ip[i].complete + '\n\n' +
                    "-----------------------------------------------------------------------------------------------------------------------"
                )

    def ViewInfo(self) :
        myViewInformation.setup(self)
        myViewInformation.show()
        
    def getMainMenuListClickedInfo(self) :
        return self.MainMenuList.currentItem().text()

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
        global userid
        userid = email

        # 로그인 기능
        login = login_function.sign_in(sign_info['Email'],sign_info['Password'])
        if(login == -1):
            QMessageBox.about(self,'SignIn Fail','아이디나 비밀번호가 틀렸습니다.')
        elif(login == 2): # 회원로그인
            widget.setFixedHeight(615)
            widget.setFixedWidth(800)
            widget.setCurrentIndex(widget.currentIndex()+1)
        elif(login == 1): # 관리자로그인
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
        self.regionSelect.addItem("Daegu")
        
    def ClickedOkButton(self):
        email = self.EmailLine.text()
        password = self.PasswordLine.text()
        address = self.regionSelect.currentText() + " " + self.AddressLine.text()

        registration_info = {
            'Email' : email,
            'Password' : password,
            'Address' : address,
            'inlist_noti' : 0
        }
        if login_function.sign_up(registration_info) == 1:
            self.close()

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

    def setup(self,totalwindow) :

        self.textBrowser.setAcceptRichText(True)
        self.textBrowser.setOpenExternalLinks(True)

        select = totalwindow.getMainMenuListClickedInfo()

        if select == "모더나 정보" :
            self.textBrowser.setPlainText("test")
        elif select == "화이자 정보" :
            self.textBrowser.setPlainText("안녕하세요") 
           


        
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
