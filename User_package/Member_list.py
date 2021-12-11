
class Member_list:
    def __init__(self):
        self.member_list = []
         #회원가입한 Member클래스 생성 -> 생성된 클래스는 바로 list 클래스의 배열로 추가된다

    def Check_Member_id(self, email, password):
        for i in range(0, len(self.member_list)):
            if self.member_list[i] != None and email == self.member_list[i].email and password == self.member_list[i].password:
                return 2 # 회원 로그인
        
        return -1 # 회원도 아닌 경우 로그인 실패
        
        

    def insert_Member(self, Member):
        self.member_list.append(Member)