m = 0
user_list = []
password_list = []
verify = "M"
info_list = []
answer = ""
x = 0

while(m <= 10000):
    user_list.append(0)
    password_list.append.(0)
    info_list.append(0)
    m += 1

class accounts:
    __username = ""
    __balance = 0
    __password = ""

    def __init__(self, username, password):
        self.__username = username
        self.__password = password

    def setuser(self, username):
        self.username = username

    def getuser(self):
        return self.__username

    def set_password(self, password):
        self.__password = password

    def get_password(self):
        return self.__password

    def withdraw(self, amount):
        if (amount >= 0):
            self.__balance -= amount
            print("Action Completed, withdrawn %s $ ", (amount))
        else:
            print("Please enter a number which is less than 0")

    def deposit(self, amount):
        if (amount >= 0):
            self.__balance += amount
            print("Action Completed, deposited %s $ ", (amount))
        else:
            print("Enter an number greater than 0")

    def get_balance(self):
        print("Balance is %s $ ", (self.__balance))

    def get_info(self, 
