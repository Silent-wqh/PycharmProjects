class Restaurant():
    """模拟餐厅"""
    def __init__(self, restaurant_name, cuisine_type):
        """
        :param restaurant_name:
        :param cuisine_type:
        """
        self.restaurant_name =restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0


    def describe_restaurant(self):
        """描述餐厅‘名称’，‘食品种类’，‘就餐人数’"""
        print(f'{self.restaurant_name}   {self.cuisine_type}'
              f'  {self.number_served}')


    def open_restaurant(self):
        """输出‘餐厅正在营业’"""
        print('餐厅正在营业')


    def set_number_served(self, number_served):
        """设置就餐人数"""
        self.number_served = number_served


    def increment_number_served(self, number_served):
        """增加就餐人数"""
        self.number_served += number_served

class IceCreamStand(Restaurant):
    """模拟冰激凌架"""
    def __init__(self, flavors, restaurant_name, cuisine_type):
        """
        :param flavors: 冰激凌列表
        :param restaurant_name: 商店名称
        :param cuisine_type: 食品种类
        """
        self.flavors = flavors
        super(IceCreamStand, self).__init__(restaurant_name, cuisine_type)


    def show_ice_cream(self):
        """输出冰激凌店的属性"""
        for flavor in self.flavors:
            print(flavor)
        Restaurant.describe_restaurant(self)


icecream_1 = IceCreamStand(['火鸡', '飞机', '上级'], 'ji冰激凌店', '冰激凌')
icecream_1.show_ice_cream()


