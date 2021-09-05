class User():
    def __init__(self, first_name, last_name, *others):
        self.first_name = first_name
        self.last_name = last_name
        self.others = others

    def describe_user(self):
        print(f'{self.first_name} {self.last_name}  {self.others}')

    def greet_user(self):
        print(f'{self.first_name.title()} {self.last_name.title()} 您好')


user1 = User('Steve', 'Jobs', '哈哈哈')
user2 = User('泽东', '毛', '啦啦啦')

user1.describe_user()
user1.greet_user()
user2.describe_user()
user2.greet_user()

