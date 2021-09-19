while True:
    numbers = input().strip().split(' ')
    numbers[0] = int(numbers[0])
    numbers[1] = int(numbers[1])
    numbers[2] = int(numbers[2])
    numbers.sort(key=int)
    for number in numbers:
        print(number, end=' ')
    print()