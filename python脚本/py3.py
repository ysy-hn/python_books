import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import LinearLocator, FormatStrFormatter


x = []
y = []
z = []
f = open("test2.txt")
line = f.readline()
while line:
    c, d, e = line.split()
    x.append(c)
    y.append(d)
    z.append(e)
    line = f.readline()
f.close()

# string型转int型
x = [float(x) for x in x if x]
y = [float(y) for y in y if y]
z = [float(z) for z in z if z]

#定义坐标轴
fig = plt.figure()
ax = plt.axes(projection='3d')

mpl.rcParams['font.size'] = 14
mpl.rcParams['figure.figsize'] = (6, 5)
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 优化坐标轴
ax.set_xlabel('X 轴', rotation=-15)
ax.set_ylabel('Y 轴', rotation=50)
ax.set_zlabel('Z 轴', rotation=90)

surf = ax.plot_trisurf(x, y, z, linewidth=0.2, antialiased=True, cmap=plt.get_cmap('rainbow'))

ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
fig.colorbar(surf, shrink=1, pad=0.08, aspect=3, label='色条')

plt.tight_layout()
plt.savefig('py3.png')
plt.show()
