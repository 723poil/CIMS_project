class Member_list:
    def __init__(self, Member):
        self.Member = Member #회원가입한 User클래스 생성 -> 생성된 클래스는 바로 list 클래스의 배열로 추가된다

    def Check_Member_id(email, passord):
        for(i = 0; i < len(Member) ; i = i + 1)
        {
         if Member[i] != None and email == Member[i].email and password == Member[i].password:
            return 2 # 회원 로그인
         else
            return -1
        }