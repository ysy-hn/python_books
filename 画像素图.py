import os
import matplotlib.pyplot as plt
from PIL import Image


w1 = 2560  # 背景黑色图的宽度，自定义
h1 = 1600  # 背景黑色图的高度，自定义
w2 = 50    # 白色图的宽度，自定义
h2 = 50    # 白色图的宽度，自定义
h3 = 5     # 白色横线图的宽度，自定义
a = 10     # 最左侧白色图与背景黑色图的间距，自定义
b = 10     # 白色横线图与白色图的间距，自定义
w3 = int(((w1-2*a-5*w2)/4) - 2*b)  # 白色横线图的高度，默认


# 生成背景黑色图
plt.axis('off')
plt.figure(num=None, figsize=(w1, h1), dpi=1, facecolor='black', edgecolor='k')
plt.savefig('1.jpg', bbox_inches='tight', pad_inches=0)
# 生成白色图
plt.axis('off')
plt.figure(num=None, figsize=(w2, h2), dpi=1, facecolor='w', edgecolor='k')
plt.savefig('2.jpg', bbox_inches='tight', pad_inches=0)
# 生成白色横线图
plt.axis('off')
plt.figure(num=None, figsize=(w3, h3), dpi=1, facecolor='w', edgecolor='k')
plt.savefig('3.jpg', bbox_inches='tight', pad_inches=0)
# 读取背景黑色图
tu1 = Image.open('1.jpg', 'r')
# 读取白色图
tu2 = Image.open('2.jpg', 'r')
# 读取白色横线图
tu3 = Image.open('3.jpg', 'r')

# 计算白色横线图放置的位置,主要是x方向位置
offset1 = (int(a + w2 + b), int((h1 - h3) // 2))
offset2 = (int(2*w2 + a + 3*b + w3), int((h1 - h3) // 2))
offset3 = (int(3*w2 + a + 5*b + 2*w3), int((h1 - h3) // 2))
offset4 = (int(4*w2 + a + 7*b + 3*w3), int((h1 - h3) // 2))
# 计算白色图放置的位置,主要是x方向位置
loc1 = (a, int((h1 - h2) // 2))
loc2 = (int(offset1[0] + w3 + b), int((h1 - h2) // 2))
loc3 = (int(offset2[0] + w3 + b), int((h1 - h2) // 2))
loc4 = (int(offset3[0] + w3 + b), int((h1 - h2) // 2))
loc5 = (int(offset4[0] + w3 + b), int((h1 - h2) // 2))
# 将白色图和白色横线图嵌入到背景黑色图中
tu1.paste(tu2, loc1)
tu1.paste(tu2, loc2)
tu1.paste(tu2, loc3)
tu1.paste(tu2, loc4)
tu1.paste(tu2, loc5)
tu1.paste(tu3, offset1)
tu1.paste(tu3, offset2)
tu1.paste(tu3, offset3)
tu1.paste(tu3, offset4)

# 删除背景黑色图、白色图、白色横线图
os.remove('1.jpg')
os.remove('2.jpg')
os.remove('3.jpg')
# 输出想要的图
output_name = '1.bmp'
tu1.save(output_name)
img = Image.open(output_name).convert('1')  # 修改图片位深度
img.save(output_name)



