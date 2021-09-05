def make_car(manufacturer, model, **others):
    car = {}
    car['manufacturer'] = manufacturer
    car['model'] = model
    for key, value in others.items():
        car[key] = value

    return  car

car = make_car('魔界', '火龙', color='红', optional_accessories='WS-10')
print(car)