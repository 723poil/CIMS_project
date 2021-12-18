from firebase_admin import db
import sys, os
sys.path.append(os.path.dirname( os.path.abspath( os.path.dirname(__file__) ) ))

import Covid_package.Corona as Corona
import Covid_package.Event as Event
import Covid_package.Infected_person as Ip
import Covid_package.News as News
import Covid_package.quarantine_Measures as Qm
import Covid_package.Vaccine as Vaccine
import firebase_application

dir = db.reference('COVID-package/')

dt = dir.get()

def get_corona():
    return Corona.Corona(dt['COVID-19'])

