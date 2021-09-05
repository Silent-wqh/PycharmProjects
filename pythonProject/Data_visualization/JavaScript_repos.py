import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# 获取API响应
url = 'https://api.github.com/search/repositories?q=language:JavaScript&sort=stars'
r = requests.get(url)
print(f'状态码(Status Code): {r.status_code}')

# 将数据加载到变量
response_dict = r.json()  # r里面是json格式的字符串，此语句是将json数据加载到变量中
print(f'总仓库数量: {response_dict["total_count"]}')

# 探索仓库
repo_dicts = response_dict['items']  # 键items对应的值是一个包含许多字典的列表
print(f'返回仓库数量: {len(repo_dicts)}')  # 返回字典键的数量

serial_num = 1  # 仓库序号
for repo_dict in repo_dicts:
    print(f'\n关于第{serial_num}个仓库的筛选信息')
    serial_num += 1
    print(f'仓库名: {repo_dict["name"]}')
    print(f'拥有者: {repo_dict["owner"]["login"]}')
    print(f'星标数: {repo_dict["stargazers_count"]}')
    print(f'仓库链接: {repo_dict["html_url"]}')
    print(f'创建时间: {repo_dict["created_at"]}')
    print(f'最近更新时间: {repo_dict["updated_at"]}')
    print(f'仓库描述: {repo_dict["description"]}')

names, plot_dicts = [], []  # 存储仓库名的列表names和存储绘制信息的列表plot_dicts
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])

    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': repo_dict['description'],
        'xlink': repo_dict['html_url']
    }
    plot_dicts.append(plot_dict)

# 可视化
my_style = LS('#333366', base_style=LCS)

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
chart.title = 'GitHub上最受关注的JavaScript项目'
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file('JavaScript_repos.svg')
