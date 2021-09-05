favorite_languages = {'Amy': 'C',
               'Bob': 'Python',
               'Cindy': 'Java',
               'David': 'Ruby',
               'Einstein': 'Pascal'
               }

persons = ['Amy', 'Bob', 'Cindy', 'David', 'Einstein',
          'Frank', 'Gaga', 'Harry']

for key in persons:
    if key in favorite_languages.keys():
        print(f'{key} 谢谢参加调查.')
    else:
        print(f'{key} 请问你可以参加调查吗?')
