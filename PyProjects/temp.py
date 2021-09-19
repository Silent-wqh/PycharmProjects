n=int(input())
s=int(input())
m=int(input())
i=0
while i<m:
    line = input().strip().split()
    a=int(line[0])
    b=int(line[1])
    i=i+1
    if a == 0:
        s=(n+s-b)%n
    else:
        s=(s+b)%n
if n==1:
    print(1)
else:
    print(s)