budgets = []  # 每月预算
curr_money = 0  # 当前持有的钱
total_money = 0  # 总持有的钱
for _ in range(12):
    budgets.append(int(input().strip()))

for i in range(12):
    curr_money += 300
    # print(f'余下{i} ____ {(curr_money - budgets[i])}')
    if (curr_money - budgets[i]) >= 100:
        total_money += (((curr_money - budgets[i])/100)) * 100
        curr_money -= (((curr_money - budgets[i])/100)) * 100
    # print(f'总共{total_money} ______ {i}')
    if curr_money >= budgets[i]:
        curr_money -= budgets[i]
    else:
        curr_money = 0
        print(f'-{i+1}')
        break

    if i == 11:
        print(total_money * 1.2)


