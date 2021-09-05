def order_sandwich(*toppings):
    for topping in toppings:
        print(topping, end='  ')
    print()

order_sandwich('胡萝卜', '火腿肠', '小辣椒')
order_sandwich('西瓜')
order_sandwich('泥土', '空气')