class User():
    """模拟用户"""
    def __init__(self, first_name, last_name, *others):
        """
        :param first_name:
        :param last_name:
        :param others:
        """
        self.first_name = first_name
        self.last_name = last_name
        self.others = others
        self.login_attempts = 0


    def describe_user(self):
        """描述用户的’姓名‘，’其他属性‘"""
        if bool(self.others) == True:
            print(f'{self.first_name}  {self.last_name}  {self.others}  {self.login_attempts}')
        else:
            print(f'{self.first_name}  {self.last_name}  {self.login_attempts}')


    def greet_user(self):
        """和用户打招呼"""
        print(f'{self.first_name.title()} {self.last_name.title()} 您好')


    def increment_login_attempts(self, attempts_number):
        """尝试登录次数+1"""
        self.login_attempts += 1


    def reset_login_attempts(self):
        """将尝试登录次数重置为0"""
        self.login_attempts = 0


user_1 = User('Steve', 'Jobs')
user_1.describe_user()
user_1.greet_user()
user_1.increment_login_attempts(1)
user_1.describe_user()
user_1.reset_login_attempts()
user_1.describe_user()