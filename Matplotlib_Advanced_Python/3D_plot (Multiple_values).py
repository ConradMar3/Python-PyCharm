import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x1 = np.random.rand(5)
y1 = np.random.rand(5)
z1 = np.random.rand(5)

x2 = np.random.rand(5)
y2 = np.random.rand(5)
z2 = np.random.rand(5)

ax.scatter(x1, y1, z1, s=20, color='red', marker='^')
ax.scatter(x2, y2, z2, s=20, color='blue', marker='o')
ax.plot(x1, y1, z1, color='green')

plt.show()
# plt.savefig('3D_plot(Multiple_values.png', bbox_inches = 'tight')
