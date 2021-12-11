import User

class Member(User.User):
    def __init__ (self, user_data):
        super().__init__(user_data['Email'])

        self.email = user_data['Email']
        self.password = user_data['Password']
        self.name = user_data['Name']
        self.birth = user_data['Birth']
        self.address = user_data['Address']
        self.job = user_data['Job']
        self.phone_number = user_data['Phone number']        