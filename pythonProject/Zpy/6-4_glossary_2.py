glossary = {'list': '列表是可以修改的存储多个不可变数据的表',
            'dict': '字典是存储键-值对的表',
            'tuple': '元组是不可修改的列表',
            'if': '如果是根据条件判断的真假来决定是否执行的关键字',
            'for': 'for是遍历条件的关键字'
            }

for key, value in sorted(glossary.items()):
    print(f'key: {key}      value: {value}')

print('*' * 10)

glossary['set'] = '集合是不可重复元素的列表'
glossary['print'] = 'print 是输出'
glossary['input'] = 'input 是输入'
glossary['in'] = 'in 检测是否被包含'
glossary['not in'] = 'not in 检测是否不被包含'

for key, value in sorted(glossary.items()):
    print(f'key: {key}      value: {value}')
