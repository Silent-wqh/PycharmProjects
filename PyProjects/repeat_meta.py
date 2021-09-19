num_list = input().strip().strip('[').strip(']').split(',')
num_set = set(num_list)
if len(num_set) == len(num_list):
    print('false')
else:
    print('true')