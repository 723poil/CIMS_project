import Manager

class Manager_list:
    def __init__(self):
        self.manager_lsit = [] #회원가입한 Manager클래스 생성 -> 생성된 클래스는 바로 list 클래스의 배열로 추가된다

    def Check_Member_id(email, passord):
        for i in range(0, len(manager_list)):
            if manager_lsit[i] != None and email == manager_lsit[i].email and password == manager_lsit[i].password:
                return 2 # 회원 로그인
            else
                return -1

    def insert_manager(Manager):
        manager_list.append(Manager)

        
        