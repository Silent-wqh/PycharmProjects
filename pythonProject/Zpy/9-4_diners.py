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


restaurant_1 = Restaurant('灰太狼涮喜羊羊', '涮羊肉')
restaurant_1.describe_restaurant()
restaurant_1.number_served = 2
restaurant_1.describe_restaurant()
restaurant_1.set_number_served(3)
restaurant_1.describe_restaurant()
restaurant_1.increment_number_served(120)
restaurant_1.describe_restaurant()