# # 1-5的立方，折线图
# import matplotlib.pyplot as plt
#
#
# input_value = list(range(1, 6))
# output_value = [x**3 for x in input_value]
# plt.plot(input_value, output_value, linewidth=5)
# plt.title('Cube Number', fontsize=30)
# plt.xlabel('Number', fontsize=14)
# plt.ylabel('Cube', fontsize=14)
#
# plt.tick_params(axis='both', labelsize=20)
#
# plt.show()

# 1-5000的立方，散点图
import matplotlib.pyplot as plt


x_value = list(range(1, 5000))
y_value = [x**3 for x in x_value]

plt.scatter(x_value, y_value, c=y_value, cmap=plt.cm.cool,
            edgecolors='none', s=20)

plt.title('Cube Number', fontsize=30)
plt.xlabel('Number', fontsize=14)
plt.ylabel('Cube', fontsize=14)

plt.tick_params(axis='both', which='major', labelsize=20)

plt.axis([0, 5100, 0, 1.5e11])

plt.show()

