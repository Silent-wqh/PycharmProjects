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


class Admin(User):
    """模拟管理员"""
    def __init__(self, first_name, last_name, *others):
        """
        初始化属性
        :param first_name: 名
        :param last_name: 姓
        :param others: 其他属性
        """
        if bool(others) == True:
            super().__init__(first_name, last_name, others)
        else:
            super().__init__(first_name, last_name)
        self.privileges = ['can add post',
                           'can delete post',
                           'can ban user']


    def show_privileges(self):
        """展示管理员及其权限"""
        User.describe_user(self)
        for privilege in self.privileges:
            print(privilege, end='       ')


admin_1 = Admin('Steve', 'Jobs')
admin_1.show_privileges()