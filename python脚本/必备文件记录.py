import shutil
import os
import logging


def path_name(pathname):
    """获取同一级别的其它目录名称方法,除了程序同级目录只能有一个目录"""
    for root, dirs, files in os.walk(pathname):
        return dirs


root = os.getcwd()  # 返回当前工作目录
root_path0 = path_name(root)[0]      # 刷新获取要复制的文件夹名称1
file_list0 = os.listdir(root_path0)  # 获取要复制的文件夹名称内的文件和文件夹名1

# 必备文件输入
file_list = ['DetectionMark.dll', 'DetectionMarkConfig.ini', 'dmd_anomalyDetect.dll', 'machinevision.dll',
             'opencv_core249.dll', 'opencv_highgui249.dll', 'opencv_imgproc249.dll', 'pthreadVC2.dll', 'rdp_client.dll',
             'TextLib.dat', 'XQ.LDI.Lancher.exe.config']
file_list1 = []

# 将文件夹1与文件夹2中不同文件和文件夹复制到文件夹1副本备份中
for a in file_list:
    if a in file_list0:
        file_list1.append(a)
logging.basicConfig(level=logging.INFO, filename='必备文件日志.log')
logging.info("必备的文件：{}".format(file_list1))