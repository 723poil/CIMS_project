import firebase_application
from firebase_admin import db

fa = firebase_application.start()

class noti:
    def __init__(self):
        self.notification_list = []

    def noti_insert(self, noti_info):
        self.notification_list.append(noti_info)