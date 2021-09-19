pens=[[],[],[]]
total_money = []
total_num = int(input().strip())
pens[0] = list(input().strip().split())
pens[1] = list(input().strip().split())
pens[2] = list(input().strip().split())



def calcu(need_num, pens, current_money=0):
    for pen in pens:
        if need_num/int(pen[0]):
            curr_need_num = need_num - (need_num/int(pen[0])*int(pen[0]))
            current_money = need_num/int(pen[0]) * int(pen[1])
            calcu(curr_need_num, pens, current_money)
        else:
            for pen in pens:
                total_money.append(current_money+int(pen[1]))

calcu(total_num, pens)

total_money.sort(key=int)
print(total_money[0])


"""
for num1 in range(0, int(total_num/int(pens[0][1])+1)):
    for num2 in range(0, int(total_num/int(pens[1][1])+1)):
        for num3 in range(0, int(total_num/int(pens[2][1])+1)):
            if num1*int(pens[0][1]) + num2*int(pens[1][0]) + num3*int(pens[2][0]) >= total_num:
                total_money.append(num1*int(pens[0][1])+num2*int(pens[1][1])+num3*int(pens[2][1]))

total_money.sort(key=int)
print(total_money[0])
"""
