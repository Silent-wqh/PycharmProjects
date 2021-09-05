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