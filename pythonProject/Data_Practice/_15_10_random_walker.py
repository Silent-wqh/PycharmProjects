from random import choice


class RandomWalker:
    """随机漫步"""
    def __init__(self, walk_num=1000):

        self.walk_num = walk_num

        self.steps_x = [0]
        self.steps_y = [0]

    def walker(self):
        """开始漫步"""
        for step_num in range(self.walk_num):
            step_x = self.get_step()
            step_y = self.get_step()

            next_x = self.steps_x[-1] + step_x
            next_y = self.steps_y[-1] + step_y
            self.steps_x.append(next_x)
            self.steps_y.append(next_y)

    def get_step(self):
        """获取漫步距离"""
        direction = choice([1, -1])
        distance = choice(list(range(7)))
        return distance * direction