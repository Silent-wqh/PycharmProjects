from _15_10_die import Die

from matplotlib import pyplot as plt


die = Die()

results = list(die.roll() for roll_num in range(5000))
y_value = list(results.count(value) for value in range(1, 7))

plt.xlabel = '点数'
plt.ylabel = '次数'

plt.title = 'D6骰子点数概率'

x_value = list(x for x in range(1, 7))
x_label = list(str(x) for x in range(1, 7))

plt.plot(x_value, y_value, linewidth=1)
plt.axis([1, 6, 0, 1000])

plt.show()
