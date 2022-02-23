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

plt.figure(dpi=100, figsize=(15, 10))
plt.subplot(3, 2, 1)
plt.plot(range(565), x)
plt.xlabel('x')
plt.subplot(3, 2, 2)
plt.plot(x, y)
plt.xlabel('x&y')
plt.subplot(3, 2, 3)
plt.plot(range(565), y)
plt.xlabel('y')
plt.subplot(3, 2, 4)
plt.plot(y, z)
plt.xlabel('y&z')
plt.subplot(3, 2, 5)
plt.plot(range(565), z)
plt.xlabel('z')
plt.subplot(3, 2, 6)
plt.plot(z, x)
plt.xlabel('z&x')
plt.tight_layout()
plt.show()
plt.savefig('对比.png')
