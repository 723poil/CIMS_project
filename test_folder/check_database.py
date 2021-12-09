import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth
from firebase_admin import db

firebaseConfig = {
    'apiKey': "AIzaSyCpvL3pI1qTqMoQZpKZBnkgCGECpO90nnI",
    'authDomain': "cims-app-42e25.firebaseapp.com",
    "databaseURL": "https://cims-app-42e25-default-rtdb.firebaseio.com/",
    'projectId': "cims-app-42e25",
    'storageBucket': "cims-app-42e25.appspot.com",
    'messagingSenderId': "667947485921",
    'appId': "1:667947485921:web:8575057fd579c3ba3485a0",
    'measurementId': "G-BDVQW2R5PY"
  }

json_path = "C:/key/cims-app-42e25-firebase-adminsdk-liwv5.json"

cred = credentials.Certificate(json_path)
app = firebase_admin.initialize_app(cred, firebaseConfig)
auth.Client(app=app)

dir = db.reference()

data = dir.get()

print(data)

check_user_data = db.reference('User-package/Users/leetkdguq73navercom').get()
user_data = db.reference('User-package/Users/leetkdguq73navercom').get()

for check_ud, ud in zip(check_user_data, user_data):
    if check_ud != 'user_notifications':
        print(check_user_data[check_ud])