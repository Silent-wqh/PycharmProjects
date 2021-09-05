def describe_city(name, country='中国'):
    """描述城市的名字和所属国家"""
    print(f'{name} 是 {country} 的城市')

describe_city('上海')
describe_city('北京')
describe_city('San Francisco', 'America')