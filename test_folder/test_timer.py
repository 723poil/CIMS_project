import Check_notification as cn
import time

cn.thread_run()

while True :
    time.sleep(0.25)
    print('other_working')


# 처음 thread_run 실행 한 후 다음 thread_run 실행부터 병렬적으로 실행 됨