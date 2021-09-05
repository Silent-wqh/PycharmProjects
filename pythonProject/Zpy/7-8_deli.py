sandwich_orders = ['金枪鱼', '沙丁鱼', '鲅鱼', '凤尾鱼']
finished_sandwiches = []
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f'I made your {current_sandwich} sandwich.')
    finished_sandwiches.append(current_sandwich)
print('所有三明治都好了')
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich, end='  ')
