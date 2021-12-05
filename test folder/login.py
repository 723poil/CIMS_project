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

def sign_in(e, p, u):
    print("Wait a moment\n")

    try:
        u[0] = auth.get_user_by_email(email=e)
    except firebase_admin._auth_utils.UserNotFoundError as e:
        print('not user')
        return -1
        
    print(u[0].uid)

    dbid = ''.join(x for x in e if x not in characters)

    result = db.reference('Users/' + dbid).get()

    if e == result['Email']:
        if p == result['Password']:
            return 1

    #u[0] = auth.get_user_by_email(email=e)

    return -1

def sign_up(e, p, u):
    print("Wait a moment\n")

    u[0] = auth.create_user(uid= e, email=e, password=p)
    link = auth.generate_email_verification_link(email, action_code_settings=None)

    print(link)

    return 1

if __name__ == "__main__":
    print("1. Sing in")
    print("2. Sing up")
    print("3. Forgot Password")

    choice = int(input("Input: "))
    print()

    user = [0]

    if choice == 1:
        print("Sing in")

        while True:
            email = input("Email: ")
            pw = input("Password: ")

            if sign_in(email, pw, user) == 1:
                break

        print("Successfully signed in to TossSync!")

    elif choice == 2:
        print("Sing up")

        while True:
            email = input("Email: ")
            pw = input("Password: ")

            if sign_up(email, pw, user) == 1:
                data = {
                    'Email': email,
                    'Password': pw
                }
                dbid = ''.join(x for x in email if x not in characters)
                dir = db.reference('Users/' + dbid)
                dir.update(data)
                
                break

        print("Successfully signed up to TossSync!: " + user[0].uid)

    # elif choice == 3:
    #     print("Forgot password")

    #     while True:
    #         email = input("Email: ")

    #         if forgot_pw(email) == 1:
    #             break

    #     print("Password reset address has been sent by email.")