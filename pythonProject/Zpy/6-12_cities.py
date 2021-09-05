cities = {'上海': {'country': '中国',
                 'population': 24180000,
                 'fact': '中国国际经济、金融、贸易、航运、科技创新中心'},
          'Newyork': {'country': 'America',
                 'population': 8510000,
                 'fact': '大苹果'},
          'London': {'country': 'UK',
                 'population': 8900000,
                 'fact': '欧洲第一大城'}
          }
for name, features in cities.items():
    print(name, end=': ')
    for feature, value in features.items():
        print(feature, end=': ')
        print(value, end='  ')
    print()