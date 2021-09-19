"""while True:
    try:
        year = int(input().strip())
    except EOFError:
        break
    else:
        if (year%400==0) or (year%100!=0 and year%4==0):
            print(1)
        else:
            print(0)"""

y = int(input())
if y % 400 == 0:
    print("1")
elif y % 4 == 0 and y % 100 != 0:
    print("1")
else:
    print("0")
