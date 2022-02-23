import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

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

X, Y = np.meshgrid(x, y)
Z, a = np.meshgrid(z, x)

mpl.rcParams['font.size'] = 14
mpl.rcParams['figure.figsize'] = (6, 5)
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

fig = plt.figure()
ax = fig.gca(projection='3d')  # 生成3D Axes对象

# 优化坐标轴
ax.set_xlabel('X 轴', rotation=-15)
ax.set_ylabel('Y 轴', rotation=50)
ax.set_zlabel('Z 轴', rotation=90)
# ax.plot_surface(X, Y, Z, linewidth=0.2, antialiased=True,cmap=plt.get_cmap('rainbow'))
ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10, cmap=plt.get_cmap('rainbow'))

plt.savefig('数据.png')
plt.show()



