def city_country(name, country):
    return f'{name}, {country}'

list_city_country = []
list_city_country.append(city_country('成都', '中国'))
list_city_country.append(city_country('Newyork', 'America'))
list_city_country.append(city_country('東京', '日本'))

for _ in list_city_country:
    print(_)