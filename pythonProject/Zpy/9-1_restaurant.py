class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name =restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f'{self.restaurant_name}   {self.cuisine_type}')

    def open_restaurant(self):
        print('餐厅正在营业')

restaurant_1 = Restaurant('灰太狼涮喜羊羊', '涮羊肉')
restaurant_1.describe_restaurant()
restaurant_1.open_restaurant()