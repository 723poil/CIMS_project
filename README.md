# CIMS_project
COVID19 information management system (CIMS)

## member
 + 박지운
 + 박찬호
 + 이상협
 + 황윤호

pyrebase 사용 x -> token 사용 x -> FCM 기능 사용 불가
 + 관리자가 알림을 추가 하면 ( read : False 내용 같이 넣어서 )
 + 전체 사용자에게 전달 시
  - 사용자의 앱에서는 일정 시간마다 데이터베이스를 검사
  - read : False 일 경우 알림 게시
  - read : True 일 경우 무시
 + 특정 사용자에게 전달 시
  - 특정 사용자의 데이터베이스 안에 알림 관련 내용 추가
  - read : False 일 경우 알림 게시
  - read : True 일 경우 무시

## 회의
 + 12-05
  - 개발 방향 결정
  - 역발 배분
  - 다음 회의 시간 조율
 
 + 12-08
  - 
