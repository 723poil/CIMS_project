import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import firebase_application
from firebase_admin import db
import Report_package.Report as Report

class Report_list:
    def __init__(self):
        self.report_list = []

        report_dir = db.reference('Report-package/report/')
        report_dt = report_dir.get()

        for i in report_dt:
            self.report_list.append(Report.report(report_dt[i]))
