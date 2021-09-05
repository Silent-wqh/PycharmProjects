sandwich_orders = ['pastrami', '金枪鱼', 'pastrami', '沙丁鱼', '鲅鱼', 'pastrami', '凤尾鱼']
for sandwich_order in sandwich_orders:
    print(sandwich_order, end='  ')
print('熏牛肉卖mu lie')
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

for sandwich_order in sandwich_orders:
    print(sandwich_order, end='  ')