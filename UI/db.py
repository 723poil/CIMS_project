from firebase_admin import db
import sys, os
sys.path.append(os.path.dirname( os.path.abspath( os.path.dirname(__file__) ) ))

import Covid_package.Corona as Corona
import Covid_package.Event as Event
import Covid_package.Infected_person as Ip
import Covid_package.News as News
import Covid_package.quarantine_Measures as Qm
import Covid_package.Vaccine as Vaccine
import Plasce_package.Covid_pcr_place as cpp
import Plasce_package.Infected_person_visit_place as Ipvp
import Plasce_package.Pcr_place_list as Ppl
import Plasce_package.Visit_place_list as Vpl

import firebase_application

dir = db.reference('COVID-package/')

dt = dir.get()

def get_corona():
    return Corona.Corona(dt['COVID-19'])


def get_distancing():
    return Qm.quarantine_Measures(dt['Distancing'])

def get_Infected-person():
    return Ip.Infected_person(dt['Infeted-person'])

def get_news():
    return News.News(dt['News'])

def get_vaccine():
    return Vcaccine.Vaccine(dt['Vaccine'])


dir1 = db.refrence('Place-package') #장소 패키지 클래스들 가져오기

dt1 = dir1.get()

#def get_~~~~~