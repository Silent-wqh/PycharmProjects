class Settings:
    """设置"""

    def __init__(self):
        """初始化静态参数"""
        # 屏幕尺寸
        self.screen_width = 1024
        self.screen_height = 768
        # 屏幕颜色
        self.bg_color = (200, 200, 200)



        # 按钮颜色
        self.button_color = (206, 87, 109)
        self.text_color = (255, 255, 255)
        # 按钮尺寸
        self.button_width, self.button_height = 200, 50

        # 矩形尺寸
        self.rect_width = 50
        self.rect_height = 200
        # 矩形颜色
        self.rect_color = (20, 20, 20)


        # 子弹尺寸
        self.bullet_width = 20
        self.bullet_height = 6
        # 子弹颜色
        self.bullet_color = (255, 255, 255)

        # 子弹同屏数量
        self.bullet_allowed = 5

        # 未射中子弹数上限
        self.not_shot = 3

        # 难度递增系数
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化动态参数"""
        # 飞船速度
        self.ship_speed = 1
        # 矩形速度
        self.rect_speed = 1
        # 子弹速度
        self.bullet_speed = 2

    def increase_speed(self):
        """增快速度"""
        # 飞船速度
        self.ship_speed *= self.speedup_scale
        # 矩形速度
        self.rect_speed *= self.speedup_scale
        # 子弹速度
        self.bullet_speed *= self.speedup_scale