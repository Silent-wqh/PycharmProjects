from User import User

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
        self.privileges = Privileges()


class Privileges():
    def __init__(self):
        self.privileges = ['can add post',
                           'can delete post',
                           'can ban user']

    def show_privileges(self):
        """展示权限"""
        for privilege in self.privileges:
            print(privilege, end='       ')