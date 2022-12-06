import matplotlib.pyplot as plt

x1 = [1,2,3,4,5]
y1 = [1,2,4,8,16]

x2 = [1,2,3,4,5]
y2 = [1,3,9,13,16]

x3 = [1,2,3,4,5]
y3 = [2,4,6,8,10]

plt.plot(x1, y1, 'ro--', label='students')
plt.plot(x2, y2, 'b^-', label='grades')
plt.plot(x3, y3, 'g-', label='visitors')
plt.legend(loc='best')

plt.title('Multi_line_plot_00')
plt.xlabel('Multi_line_plot_01')
plt.ylabel('Multi_line_plot_02')
#plt.show()
plt.savefig('Multi_line_plot.png', bbox_inches='tight')