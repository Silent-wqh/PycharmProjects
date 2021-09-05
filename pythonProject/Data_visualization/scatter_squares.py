import matplotlib.pyplot as plt


x_value = list(range(1, 1001))
y_value = [x**2 for x in x_value]

# plt.scatter(x_value, y_value, c='red', edgecolors='none', s=20)
# plt.scatter(x_value, y_value, c=(0, 0, 0.8), edgecolors='none', s=20)
plt.scatter(x_value, y_value, c=y_value, cmap=plt.cm.cool,
            edgecolors='none', s=20)

# 设置图表标题并给坐标轴加上标签
plt.title('Square Number', fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Square of Value', fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=14)

# 设置每个坐标轴的取值范围
plt.axis([0, 1100, 0, 1100000])

# plt.show()
plt.savefig('squares_plot.png', bbox_inches='tight')
