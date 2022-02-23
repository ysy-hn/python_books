import shutil
import os


def path_name(pathname):
    """获取同一级别的其它目录名称方法,除了程序同级目录只能有一个目录"""
    for root, dirs, files in os.walk(pathname):
        return dirs


root = os.getcwd()  # 返回当前工作目录
root_path0 = path_name(root)[0]             # 获取要复制的文件夹名称1
root_path1 = path_name(root)[1]             # 获取要复制的文件夹名称2
make0 = root + '\\' + root_path0 + '-副本'   # 创建要复制文件夹的副本名备份1
make1 = root + '\\' + root_path1 + '-副本'   # 创建要复制文件夹的副本名备份2
os.mkdir(make0)   # 创建要复制文件夹的副本备份1
os.mkdir(make1)   # 创建要复制文件夹的副本备份2

root_path0 = path_name(root)[0]      # 刷新获取要复制的文件夹名称1
root_path1 = path_name(root)[1]      # 刷新获取要复制文件夹的副本名备份1
root_path2 = path_name(root)[2]      # 刷新获取要复制的文件夹名称2
root_path3 = path_name(root)[3]      # 刷新获取要复制文件夹的副本名备份2
file_list0 = os.listdir(root_path0)  # 获取要复制的文件夹名称内的文件和文件夹名1
file_list2 = os.listdir(root_path2)  # 获取要复制的文件夹名称内的文件和文件夹名2

path0 = root + '\\' + root_path0 + '\\'  # 获取要复制的文件夹名称路径1
path1 = root + '\\' + root_path1 + '\\'  # 获取复制的文件夹名称路径1
path2 = root + '\\' + root_path2 + '\\'  # 获取要复制的文件夹名称路径2
path3 = root + '\\' + root_path3 + '\\'  # 获取复制的文件夹名称路径2

# 将文件夹1与文件夹2中不同文件和文件夹复制到文件夹1副本备份中
for a in file_list0:
    if a not in file_list2:
        if os.path.isdir(path0+a):
            shutil.copytree(path0+a, path1+a)
        else:
            shutil.copy(path0+a, path1+a)

# 将文件夹2与文件夹1中不同文件和文件夹复制到文件夹2副本备份中
for b in file_list2:
    if b not in file_list0:
        if os.path.isdir(path2+b):
            shutil.copytree(path2+b, path3+b)
        else:
            shutil.copy(path2+b, path3+b)
