total_num = int(input().strip())
total_money = []
for i in range(3):
    pen = list(map(int, input().strip().split()))
    total_money.append(((total_num+pen[0]-1)//pen[0])*pen[1])

total_money.sort(key=int)
print(total_money[0])