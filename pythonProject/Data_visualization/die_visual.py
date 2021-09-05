import pygal

from die import Die


# 创建一个D6
die_1 = Die()
die_2 = Die()

# 掷几次骰子，并将结果存储在一个列表中
results = []
results = list(die_1.roll()*die_2.roll() for roll_num in range(50000))
# for roll_num in range(500000):
#     result = die_1.roll() + die_2.roll()
#     results.append(result)

set_num = set()

for i in range(1, 6):
    for j in range(1, 6):
        set_num.add(i*j)

list_num = sorted(list(set_num))

# 分析结果
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
frequencies = list(results.count(value) for value in range(1, 37))
# for value in range(2, max_result+1):
#     frequency = results.count(value)
#     frequencies.append(frequency)

hist = pygal.Bar()

hist.title = "Results of rolling one D6 1000 times."
hist.x_labels = list(str(x) for x in range(1, 37))
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'

hist.add('D6 + D6 + D6', frequencies)
hist.render_to_file('dice_visual.svg')