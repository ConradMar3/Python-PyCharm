import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [1,2,4,8,16]

plt.plot(x, y, 'b--^', linewidth =3.0)
plt.title('Line_plot')
plt.xlabel('Line_Plot_Horizontal_Title')
plt.ylabel('Line_Plot_Vertical_Title')
#plt.show()
plt.savefig('line_plot.png', bbox_inches='tight')