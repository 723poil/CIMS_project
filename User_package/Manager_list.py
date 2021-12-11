
class Manager_list:
    def __init__(self):
        self.manager_lsit = [] #회원가입한 Manager클래스 생성 -> 생성된 클래스는 바로 list 클래스의 배열로 추가된다

    def Check_Manager_id(self, email, password):
        for i in range(0, len(self.manager_list)):
            if self.manager_lsit[i] != None and email == self.manager_lsit[i].email and password == self.manager_lsit[i].password:
                return 2 # 관리자 로그인
        
        return -1 # 관리자가 아닌 경우 회원 로그인으로 시도

    def insert_manager(self, Manager):
        self.manager_list.append(Manager)

        
        