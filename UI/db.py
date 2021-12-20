from firebase_admin import db
import sys, os
sys.path.append(os.path.dirname( os.path.abspath( os.path.dirname(__file__) ) ))

import Covid_package.Corona as Corona
import Covid_package.Event as Event
import Covid_package.Infected_person as Ip
import Covid_package.News as News
import Covid_package.quarantine_Measures as Qm
import Covid_package.Vaccine as Vaccine
import Place_package.Pcr_place_list as Ppl
import Place_package.visit_place_list as Vpl
import Report_package.Report_list as Rl
import Notification_package.notification_list as nl

import firebase_application

# firebase_application.start()

COVID_dir = db.reference('COVID-package/')
PLACE_dir = db.reference('Place-package/')
REPORT_dir = db.reference('Report-package/')

COVID_dt = COVID_dir.get()
PLACE_dt = PLACE_dir.get()
REPORT_dt = REPORT_dir.get()

def get_corona():
    return Corona.Corona(COVID_dt['COVID-19'])

def get_distancing():
    return Qm.quarantine_Measures(COVID_dt['Distancing'])

def get_Infected_person():
    ip = dict()
    for i in COVID_dt['Infected-person']:
        ip.update({
            i : Ip.Infected_person(COVID_dt['Infected-person'][i])
        })
    return ip

def get_news():
    news = []
    for i in range(len(COVID_dt['News'])):
        news.append(News.News(COVID_dt['News'][i]))
    return news

def get_vaccine():
    vaccine =dict()
    for i in COVID_dt['Vaccine']:
        vaccine.update({i : Vaccine.Vaccine(COVID_dt['Vaccine'][i])})
    return vaccine

def get_event():
    event = dict()
    for i in COVID_dt['event']:
        a = []
        for j in range(1, len(COVID_dt['event'][i])):
            a.append(Event.Event(COVID_dt['event'][i][j]))
            event.update({
                i : a
            })
    return event

def get_ppl(userid):
    characters = '@.'
    userid_dbref = ''.join(x for x in userid if x not in characters)
    user_dir = db.reference('User-package/Users/' + userid_dbref)
    user_dt = user_dir.get()
    user_address = user_dt['Address']
    return Ppl.pcr_list(user_address)


def get_vpl(userid):
    characters = '@.'
    userid_dbref = ''.join(x for x in userid if x not in characters)
    user_dir = db.reference('User-package/Users/' + userid_dbref)
    user_dt = user_dir.get()
    user_address = user_dt['Address']
    return Vpl.visit_list(user_address)

def get_rl():
    return Rl.Report_list()

def get_nl(userid):
    noti = nl.noti()
    noti.set_noti_list(userid)
    return noti

# u = get_vpl('leetkdguq73@naver.com')
# print(u.user_address)
# for i in u.vl:
#     print(i.address)
#     print(i.visit_time)

# u = get_rl()
# for i in u.report_list:
#     print(i.content)
#     print(i.date)
#     print(i.user)

# u = get_nl('leetkdguq73@naver.com')
# for i in u.notification_list:
#     print(i['title'])
#     print(i['content'])
#     print(i['date'])