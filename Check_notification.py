# 주기적으로 알람 확인 코드
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import User_package.notification_list
# import firebase_application
from firebase_admin import db
import threading

# fa = firebase_application.start()

characters = "@."

def thread_run(args):
    # args = [uid, notilist]
    # 1. 개인 알림 확인 과 공통 알림 확인 코드 작성
    #1. 개인 알림 확인
    db_user_id = ''.join(x for x in args[0] if x not in characters)

    user_noti = db.reference('User-package/Users/' + db_user_id + '/user_notifications/').get()

    for i in user_noti:
        if user_noti[i]['isinlist'] == 'no':
            # 알림 창에 추가
            # 추가 후 isinlist 값 변경
            args[1].noti_insert(user_noti[i])
            dir = db.reference('User-package/Users/' + db_user_id + '/user_notifications/' + i)
            user_noti[i]['isinlist'] = 'yes'
            dir.update(user_noti[i])
            print('개인 알림 추가')
    
    #2. 공통 알림 확인
    public_noti = db.reference('User-package/All-notifications/').get()
    user_noti = db.reference('User-package/Users/' + db_user_id).get()
    user_noti_count = user_noti['inlist_noti']

    if public_noti['noti_count'] != user_noti_count:
        # 알림 창에 추가
        # 추가 후 user_noti_count 변경
        while public_noti['noti_count'] != user_noti_count:
            args[1].noti_insert(public_noti[str(user_noti_count+1)])
            user_noti_count += 1
        
        dir = db.reference('User-package/Users/' + db_user_id)
        user_noti['inlist_noti'] = user_noti_count
        dir.update(user_noti)

        print('공통 알림 추가')

    # 간격 일단 1분마다 설정
    threading.Timer(60, thread_run, args).start()

nl = User_package.notification_list.noti()
thread_run(['leetkdguq73@naver.com', nl])