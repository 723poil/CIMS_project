import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth
from firebase_admin import db

# firebase web app 생성 시 뜨는 정보 가져온 것
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

# 새 비공개 키 저장한 곳 ( 통일 합시다 )
json_path = "C:/key/cims-app-42e25-firebase-adminsdk-liwv5.json"

cred = credentials.Certificate(json_path)
app = firebase_admin.initialize_app(cred, firebaseConfig)
auth.Client(app=app)

characters = "@."

dir = db.reference('Users/leetkdguq73navercom/vaccine-aya/')
dir.update(
    {
        'title' : 'blabla',
        'content' : 'blabla'
    } 
)