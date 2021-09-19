try:
    nums = input().strip().split()
    num_l = nums[0]
    num_r = nums[1]
except EOFError:
    pass
else:
    times = 0 # 统计2出现的次数
    for num in range(int(num_l), int(num_r)+1):
        k = len(str(num)) - 1  # 幂
        temp_num = num
        while (temp_num + 9) // 10:
            temp = temp_num % 10
            if temp == 2:
                times += 1
            temp_num = temp_num // 10

    print(times)