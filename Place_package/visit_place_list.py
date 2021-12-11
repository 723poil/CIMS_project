import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import firebase_application
from firebase_admin import db
import Infected_person_visit_place as vp

fa = firebase_application.start()

class visit_list:
    def __init__(self, user_address):
        self.user_address = user_address
        self.vl = []

        set_area = ['Gyeonggi-do', 'Gangwon-do', 'Chungcheong-do', 'Jeolla-do', 'Gyeongsang-do']

        set_comp = False

        ua = user_address.split()

        for i in set_area:
            if i == ua:
                set_comp = True
                break
        
        if set_comp == True:
            set_place = db.reference('Place-package/infected_visit_place/' + ua[0] + ua[1]).get()
        else :
            set_place = db.reference('Place-package/infected_visit_place/' + ua[0]).get()

        for i in set_place:
            self.vl.append(vp.ipvp(set_place[i]))

vll = visit_list('Daegu')

for i in vll.vl:
    print(i.visit_time + '\n' + i.address + '\n' + i.ischeck_contact_complete)