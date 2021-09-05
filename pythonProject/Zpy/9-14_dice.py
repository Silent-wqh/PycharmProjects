from random import randint

class Die():
    """骰子模拟器"""
    def __init__(self, sides = 6):
        """
        初始化
        self.sides: 骰子的面数
        """
        self.sides = sides


    def roll_die(self):
        print(randint(1, self.sides + 1))


die_1 = Die(6)
for _ in range(10):
    die_1.roll_die()
print('*' * 20)

die_2 = Die(10)
for _ in range(10):
    die_2.roll_die()
print('*' * 20)

die_3 = Die(20)
for _ in range(10):
    die_3.roll_die()