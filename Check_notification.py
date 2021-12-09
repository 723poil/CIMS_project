# 주기적으로 알람 확인 코드
import time
import threading

count = 0

def thread_run():
    # 1. 개인 알림 확인 과 공통 알림 확인 코드 작성
    
    # 간격 일단 1분마다 설정
    threading.Timer(60, thread_run).start()