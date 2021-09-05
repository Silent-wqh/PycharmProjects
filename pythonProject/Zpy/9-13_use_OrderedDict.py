from collections import OrderedDict

glossary = OrderedDict()
glossary['list'] = '列表是可以修改的存储多个不可变数据的表'
glossary['dict'] = '字典是存储键-值对的表'
glossary['if'] = '如果是根据条件判断的真假来决定是否执行的关键字'

for key, value in glossary.items():
    print(f'{key}  {value}')
