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

import firebase_application

COVID_dir = db.reference('COVID-package/')
PLACE_dir = db.reference('Place-package/')

COVID_dt = COVID_dir.get()
PLACE_dt = PLACE_dir.get()

def get_corona():
    return Corona.Corona(COVID_dt['COVID-19'])

def get_distancing():
    return Qm.quarantine_Measures(COVID_dt['Distancing'])

def get_Infected_person():
    return Ip.Infected_person(COVID_dt['Infeted-person'])

def get_news():
    return News.News(COVID_dt['News'])

def get_vaccine():
    return Vaccine.Vaccin(COVID_dt['Vaccine'])