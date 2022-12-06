import matplotlib.pyplot as plt

#Using a loop to do calculations
x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()

#Defining custom colors ( add 'c=?' to scatter())
#'C=(0,0,0)' is the RGB model.
#ax.scatter(x_values, y_values, c='green', s=10)

#Using a colormap
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

#Set chart title and label axes
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

#Set the range of each axis
ax.axis([0, 1100, 0, 1100000])

#plt.show()

#Saving plot automatically: use 'plt.savefig()'
plt.savefig('Defining_colors.png', bbox_inches='tight')

#Note: 'plt.savefig()' creates a .png file.