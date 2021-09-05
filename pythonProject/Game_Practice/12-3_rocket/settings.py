class Settings:
    """存储设置"""
    def __init__(self):

        # 屏幕尺寸
        self.screen_width = 1024
        self.screen_height = 768

        # 背景色
        self.bg_color = (22, 119, 179)

        # 火箭速度
        self.move_speed = 0.5

        # 子弹属性
        self.bullet_speed_factor = 1
        self.bullet_height = 3
        self.bullet_width = 15
        self.bullet_allowed = 3
        # 设置为 random ，即发射彩色子弹
        self.bullet_color = 'random'
        # self.bullet_color = (60, 60, 60)
