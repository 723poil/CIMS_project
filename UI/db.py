from firebase_admin import db
import sys, os
sys.path.append(os.path.dirname( os.path.abspath( os.path.dirname(__file__) ) ))

import Covid_package.Corona as Corona
import Covid_package.Event as Event
import Covid_package.Infected_person as Ip
import Covid_package.News as News
import Covid_package.quarantine_Measures as Qm
import Covid_package.Vaccine as Vaccine
import Place_package.Covid_pcr_place as cpp
import Place_package.Infected_person_visit_place as Ipvp
import Place_package.Pcr_place_list as Ppl
import Place_package.visit_place_list as Vpl
import Report_package.Report_list as Rl
import User_package.notification_list as nl

import firebase_application

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
    return Ip.Infected_person(COVID_dt['Infeted-person'])

def get_news():
    return News.News(COVID_dt['News'])

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