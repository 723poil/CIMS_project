import firebase_application
from firebase_admin import db

class noti:
    def __init__(self):
        self.notification_list = []

    def set_noti_list(self, userid):
        characters = "@."
        
        db_user_id = ''.join(x for x in userid if x not in characters)

        # 1. 개인 알림 확인
        user_noti = db.reference('User-package/Users/' + db_user_id + '/user_notifications/').get()

        if user_noti != None:

            for i in user_noti:
                if user_noti[i]['read'] == "false":
                    self.notification_list.append(user_noti[i])
                    dir = db.reference('User-package/Users/' + db_user_id + '/user_notifications/' + i)
                    user_noti[i]['isinlist'] = 'yes'
                    dir.update(user_noti[i])
                    print('개인 알림 추가')
                
        # 2. 공통 알림 확인
        public_noti = db.reference('User-package/All-notifications/').get()
        user_noti = db.reference('User-package/Users/' + db_user_id).get()
        user_noti_count = int(public_noti['noti_count'])

        for i in range(1,user_noti_count+1):
            self.notification_list.append(public_noti[str(i)])
        
        dir = db.reference('User-package/Users/' + db_user_id)
        user_noti['inlist_noti'] = user_noti_count
        dir.update(user_noti)

        print('공통 알림 추가')

    # 알림 리스트 구성 ( argument -> userid )
    def check_noti(self, userid):
        
        characters = "@."
        
        db_user_id = ''.join(x for x in userid if x not in characters)

        # 1. 개인 알림 확인
        user_noti = db.reference('User-package/Users/' + db_user_id + '/user_notifications/').get()

        if user_noti != None:

            for i in user_noti:
                if user_noti[i]['isinlist'] == 'no':
                    self.notification_list.append(user_noti[i])
                    dir = db.reference('User-package/Users/' + db_user_id + '/user_notifications/' + i)
                    user_noti[i]['isinlist'] = 'yes'
                    dir.update(user_noti[i])
                    print('개인 알림 추가')
                
        # 2. 공통 알림 확인
        public_noti = db.reference('User-package/All-notifications/').get()
        user_noti = db.reference('User-package/Users/' + db_user_id).get()
        user_noti_count = user_noti['inlist_noti']

        if int(public_noti['noti_count']) != user_noti_count:
            # 추가 후 user_noti_count 변경
            while public_noti['noti_count'] != user_noti_count:
                self.notification_list.append(public_noti[str(user_noti_count+1)])
                user_noti_count += 1
            
            dir = db.reference('User-package/Users/' + db_user_id)
            user_noti['inlist_noti'] = user_noti_count
            dir.update(user_noti)

            print('공통 알림 추가')