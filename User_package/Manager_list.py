class Manager_list:
    def __init__(self, Manager):
        self.Manager = Manager #회원가입한 User클래스 생성 -> 생성된 클래스는 바로 list 클래스의 배열로 추가된다

    def Check_Member_id(email, passord):
        for(i = 0; i < len(Manager) ; i = i + 1)
        {
         if Manager[i] != None and email == Manager[i].email and password == Manager[i].password:
            return 2 # 회원 로그인
         else
            return -1
        }