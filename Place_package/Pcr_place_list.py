import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import firebase_application
from firebase_admin import db
import Covid_pcr_place as cp

fa = firebase_application.start()

class pcr_list:
    def __init__(self, user_address):
        self.user_address = user_address
        self.pl = []

        set_area = ['Gyeonggi-do', 'Gangwon-do', 'Chungcheong-do', 'Jeolla-do', 'Gyeongsang-do']

        set_comp = False

        ua = user_address.split()

        for i in set_area:
            if i == ua:
                set_comp = True
                break
        
        if set_comp == True:
            set_place = db.reference('Place-package/Covid_pcr_place/' + ua[0] + ua[1]).get()
        else :
            set_place = db.reference('Place-package/Covid_pcr_place/' + ua[0]).get()

        for i in set_place:
            self.pl.append(cp.cpp(set_place[i]))

pll = pcr_list('Daegu')

for i in pll.pl:
    print(i.time + '\n' + i.address)