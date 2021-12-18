import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import firebase_application
from firebase_admin import db

characters = "@."

class report:
    
    def __init__(self, content, date, user):
        self.content = content
        self.date = date
        self.user = user

    def reportit(self):
        dbid = ''.join(x for x in self.user if x not in characters)
        dir = db.reference("Report-package/report/")
        dir.push({
            'content' : self.content,
            'date' : self.date,
            'user' : self.user
            })
r = report('bla', 'bla', 'asdnavercom')

r.reportit()
