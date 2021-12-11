import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import firebase_application
import firebase_admin
from firebase_admin import db

fa = firebase_application.start()

characters = "@."

def sign_in(email, password):
    
    try:
        fa.get_user_by_email(email=email)
    except firebase_admin._auth_utils.UserNotFoundError as e:
        print('not user')
        return -1

    db_user_id = ''.join(x for x in email if x not in characters)

    result = db.reference('Users/Manager/' + db_user_id).get()

    if result != None and email == result['Email'] and password == result['Password']:
        return 1 # 관리자 로그인
    else:
        result = db.reference('Users/Member/' + db_user_id).get()

        if result != None and email == result['Email'] and password == result['Password']:
            return 2 # 회원 로그인
    
    # return 값으로 구분하여 Manager와 Member 생성자를 만들어야 할듯 (밑에 예시)
    # user = Manager.Manager(user_data))
    # user = Member.Member(user_data)

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

    user = fa.create_user(uid = registration_info['Email'], email=registration_info['Email'], password=registration_info['Password'])
    
    if user is None:
        return -1
    
    link = fa.generate_email_verification_link(user.email, action_code_settings=None)
    print(link) # link 들어가서 이메일 검증하는 단계 만들기

    user_data = {
        'Email' : registration_info['Email'],
        'Password' : registration_info['Password'],
        'Name' : registration_info['Name'],
        'Birth' : registration_info['Birth'],
        'Address' : registration_info['Address'],
        'Job' : registration_info['Job'],
        'Phone number' : registration_info['Phone number'],
    }

    db_user_id = ''.join(x for x in registration_info['Email'] if x not in characters)
    
    user_dir = db.reference('User-package/Users/' + db_user_id)
    user_dir.update(user_data)

    check_user_data = db.reference('User-package/Users/' + db_user_id).get()

    # 사용자 등록은 정상적으로 되었지만, 데이터베이스에 정보가 제대로 안들어갔을 경우
    # 등록된 정보를 제거 한 후 다시 회원가입 하도록 유도
    for check_ud, ud in zip(check_user_data, user_data):
        if check_ud != 'user_notifications' and check_user_data[check_ud] != user_data[ud]:
            print('sign up failed')
            fa.delete_user(uid=registration_info['Email'])
            return -1
    
    return 1

def search_Id():
    pass

def search_Password():
    pass

# 비밀번호 찾기, 아이디 찾기 기능 추가 예정
# 클래스 다이어그램 상의 관리자 리스트와 회원 리스트 클래스들은 데이터베이스로 대체
# checkidvali 클래스 -> 클래스 다이어그램에서 지워야함