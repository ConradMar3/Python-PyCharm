import matplotlib.pyplot as plt

plt.style.use('seaborn')
print(plt.style.available)

x1 = [1, 2, 3, 4, 5]
y1 = [1, 2, 4, 8, 16]

plt.bar(x1, y1)
plt.title('Your title')
plt.xlabel('Horizontal title')
plt.ylabel('Vertical title')

# plt.show()
plt.savefig('Themes.png', bbox_inches='tight')
