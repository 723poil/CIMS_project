# CIMS_project
+ COVID19 information management system (CIMS)

---------------------------------------
## 사용 언어
### Python 3.9.0

## member
 + 박지운
 + 박찬호
 + 이상협
 + 황윤호

## 회의
 + 12-05
 
   - 개발 방향 결정
   - 역발 분배 ( 프론트엔드 - 박찬호, 황윤호 || 백엔드 - 박지운, 이상협 )
   - 다음 회의 시간 조율
 
 + 12-08
 
   - 데이터베이스 구조 구축
   - UI 시작
   - Class diagram 수정

 + 12-11

   - 주기 알림 체크, 회원 리스트, 관리자 리스트, 장소 리스트, 신고 리스트 파일 작성
   - 전체적이 UI 작성 완료
   - UI 간 연결

 + 12-18

   - 클래스 다이어그램 수정 및 연관 클래스 attribute 수정
   - 로그인UI와 로그인 기능 연결 및 확인
   - 회원가입UI와 회원가입 기능 연결 및 확인
   - diplayview UI와 관련 기능 연결 및 확인
   - 파일 경로 수정

 + 12-20

   - 리스트 들과 ui 연결
   - 기본알림과 신고알림 기능 추가
   - 프로그램 완성
   - 발표 촬영 및 보고서 작성
    
## 문제점과 해결책

### 1. pyrebase 사용 x -> token 사용 x -> FCM 기능 사용 불가
 + 관리자가 알림을 추가 하면 ( read : False 내용 같이 넣어서 )
 + 전체 사용자에게 전달 시
 
   - 사용자의 앱에서는 일정 시간마다 데이터베이스를 검사
   - read : False 일 경우 알림 게시
   - read : True 일 경우 무시
 + 특정 사용자에게 전달 시
 
   - 특정 사용자의 데이터베이스 안에 알림 관련 내용 추가
   - read : False 일 경우 알림 게시
   - read : True 일 경우 무시
 + 쓰레드를 이용해 주기적으로 알림 유무 체크
 
   - 참고자료 : https://niceman.tistory.com/144

 --> 쓰레드를 사용하지 않고, 알림 버튼을 클릭할때 확인을 하여 넣어주기로 함.

### 2. 자바 상에서의 패키지 개념을 어떻게 파이썬에서 표현 할 것인가?
+ 폴더로 나누어서 표현

## 사용한 API

### firebase
    #firebase install
    
    python -m pip install firebase-admin
### PyQt5 (python gui)
    #PyQt5 install
    
    python -m pip install PyQt5


## 사용방법
> 경로설정
>> C:/CIMS_PROJECT/ 에 파일 저장  
>> C:/key/ 에 지급된 비공개 키 저장  

> 멤버로 로그인 할 경우  
>> 회원가입 진행  

> 관리자로 로그인 할 경우
>> id : manager@knu.ac.kr  
>> pass : 123456
