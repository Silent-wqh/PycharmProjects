import time

# 在此导入time库，并在开头设置开始时间


a = input().strip().split()
start = time.perf_counter()
print(int(a[0]) + int(a[1]))

end = time.perf_counter()
# 在程序运行结束的位置添加结束时间
print("运行耗时", end-start)
# 再将其进行打印，即可显示出程序完成的运行耗时