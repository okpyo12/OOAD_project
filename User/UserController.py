from User.User import User

class UserController(User):

    def __init__(self):
        self.user = User()

    def settingCarNum(self, num):
        self.user.setCarNum(num)

    def gettingCarNum(self):
        return self.user.getCarNum()

    def plusCarNum(self):
        self.user.setCarNum(self.user.getCarNumber() + 1)
    
    def savingDB(self, num):
        self.user.saveDB(num)