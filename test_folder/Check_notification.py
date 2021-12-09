# 주기적으로 알람 확인 코드
import time
import threading

count = 0

def thread_run():
    global count
    # 1. 개인 알림 확인 과 공통 알림 확인 코드 작성
    print('====',time.ctime(),'====')
    count += 1
    for i in range(1, 51):
        time.sleep(0.1)
        print('Thread running - ', i)

    if count != 50:
        threading.Timer(2.5, thread_run).start()