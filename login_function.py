import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth
from firebase_admin import db
import Manager
import Member

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

characters = "@."

def sign_in(email, password, user):
    
    try:
        user = auth.get_user_by_email(email=email)
    except firebase_admin._auth_utils.UserNotFoundError as e:
        print('not user')
        return -1

    db_user_id = ''.join(x for x in email if x not in characters)

    result = db.reference('Users/Manager/' + db_user_id).get()

    if result != None and email == result['Email'] and password == result['Password']:
        user = Manager.Manager(result)
        return user # 관리자 로그인
    else:
        result = db.reference('Users/Member/' + db_user_id).get()

        if result != None and email == result['Email'] and password == result['Password']:
            user = Member.Member(result)
            return user # 회원 로그인
    
    # 관리자와 회원 return 부분은 바꾸어야 할듯
    # return 값으로 구분하여 Manager와 Member 생성자를 만들어야 할듯

    return -1 # 등록되지 않은 아이디 및 비밀번호

def sign_up(registration_info): # 클래스 다이어그램에 나와있는 정보를 sign_up 에서 등록
    # registration_info = {
    #   'Email' : '',
    #   'Password' : '',
    #   'Address' : '',
    #   'Phone number' : '',
    #   'Age' : '',
    #   ...
    # }
    # 형식으로 가져와서 수행한다.

    user = auth.create_user(uid = registration_info['Email'], email=registration_info['Email'], password=registration_info['Password'])
    
    if user == None:
        return -1
    
    link = auth.generate_email_verification_link(user.email, action_code_settings=None)
    print(link) # link 들어가서 이메일 검증하는 단계 만들기

    user_data = {
        'Email' : registration_info['Email'],
        'Password' : registration_info['Password'],
        'Name' : registration_info['Name'],
        'Birth' : registration_info['Birth'],
        'Address' : registration_info['Address'],
        'Job' : registration_info['Job'],
        'Resident registration number' : registration_info['Resident registration number'],
        'Phone number' : registration_info['Phone number'],
    }

    db_user_id = ''.join(x for x in registration_info['Email'] if x not in characters)
    
    user_dir = db.reference('Users/Member/' + db_user_id)
    user_dir.update(user_data)

    check_user_data = db.reference('Users/Member' + db_user_id).get()

    for c, u in check_user_data, user_data:
        if c != u:
            print('sign up failed')
            auth.delete_user(uid=registration_info['Email'])
            return -1
    
    return 1

# 회원가입, 비밀번호 찾기, 아이디 찾기 기능 추가 예정
# 클래스 다이어그램 상의 관리자 리스트와 회원 리스트 클래스들은 데이터베이스로 대체
# checkidvali 클래스 -> 클래스 다이어그램에서 지워야함