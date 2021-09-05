rivers = {'nile': 'egypt',
          '黄河': '中国',
          '长江': '中国'}

for key, value in rivers.items():
    print(f'The {key} runs through {value}')

for key in rivers.keys():
    print(key)

for value in rivers.values():
    print(value)