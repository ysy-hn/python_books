import os
import shutil
import logging


def path_name(pathname):
    """获取同一级别的其它目录名称方法,除了程序同级目录只能有一个目录"""
    for root, dirs, files in os.walk(pathname):
        for dir in dirs:
            dir = dir + '/'
            return dir


class DeleteFileDir:
    def __init__(self, root_path, file_list, dir_list, del_file=[], del_dir=[]):
        self.root_path = root_path
        self.file_list = file_list
        self.dir_list = dir_list
        self.del_file = del_file
        self.del_dir = del_dir

    def get_file_path(self):
        """递归遍历文件夹里面所有内容，包括文件夹和文件，file_list是放文件的、dir_list是放目录的"""
        dir_or_files = os.listdir(self.root_path)  # 获取文件和文件夹名称并整理为列表
        for dir_file in dir_or_files:
            dir_file_path = os.path.join(self.root_path, dir_file)  # 获取文件夹或者文件的路径
            if os.path.isdir(dir_file_path):  # 判断该路径为文件还是路径
                self.dir_list.append(dir_file_path)
                # get_file_path(dir_file_path, file_list, dir_list)  # 递归获取所有文件和目录的路径
            else:
                self.file_list.append(dir_file_path)

    def delete_file(self, del_file_lists, needfile_list):
        """删除文件方法"""
        needfile_list1 = []
        for file_name in self.file_list:
            if not (file_name.endswith('.dll') or file_name.endswith('.dat') or file_name.endswith('.txt') or
                    file_name.endswith('.ini') or file_name.endswith('.xml') or file_name.endswith('.exe') or
                    file_name.endswith('.config')):
                self.del_file.append(file_name.lstrip(self.root_path))
                os.remove(file_name)
            elif file_name in del_file_lists:
                self.del_file.append(file_name.lstrip(self.root_path))
                os.remove(file_name)
            elif file_name in needfile_list:
                file_name = file_name[file_name.index('/')+1:]
                needfile_list1.append(file_name)
        logging.basicConfig(level=logging.INFO, filename='删除日志.log')
        logging.info("已删除的文件：{}".format(self.del_file))  # 打印删除的文件日志
        logging.info("必备的文件：共{}个文件，具体：{}".format(len(needfile_list1), needfile_list1))

    def delete_dir(self, del_dir_lists, needdir_list):
        """删除文件夹方法"""
        needdir_list1 = []
        for dir_name in self.dir_list:
            if dir_name in del_dir_lists:
                self.del_dir.append(dir_name.lstrip(self.root_path))
                shutil.rmtree(dir_name, True)
            elif dir_name in needdir_list:
                dir_name = dir_name[dir_name.index('/')+1:]
                needdir_list1.append(dir_name)
        logging.info("已删除的文件夹：{}".format(self.del_dir))  # 打印删除的文件夹日志
        logging.info("必备的文件夹：共{}个文件，具体：{}".format(len(needdir_list1), needdir_list1))


file_list = []
dir_list = []
root = os.getcwd()  # 返回当前工作目录
root_path = path_name(root)  # 将同一级别的其它目录赋值给root_path

# 指定要删除的文件名称
del_file_list = ['AppUpdater.exe']
# 指定要删除的文件夹名称
del_dir_list = ['de', 'en', 'en-US', 'ErrorImages', 'es', 'fr', 'it', 'ja', 'JobFiles', 'JobMake', 'ko', 'logs',
                'MatchedMarks', 'PrintFiles']
# 必备文件输入
needfile_list = ['DetectionMark.dll', 'DetectionMarkConfig.ini', 'dmd_anomalyDetect.dll', 'machinevision.dll',
             'opencv_core249.dll', 'opencv_highgui249.dll', 'opencv_imgproc249.dll', 'pthreadVC2.dll', 'rdp_client.dll',
             'TextLib.dat', 'XQ.LDI.Lancher.exe.config']
# 必备文件夹输入
needdir_list = ['configs', 'data', 'Langs', 'patterns',  'x64', 'x86', 'zh-Hans', 'zh-Hant']

del_file_lists = [root_path + x for x in del_file_list]
del_dir_lists = [root_path + x for x in del_dir_list]
needfile_lists = [root_path + x for x in needfile_list]
needdir_list = [root_path + x for x in needdir_list]

file_dir = DeleteFileDir(root_path, file_list, dir_list)
file_dir.get_file_path()  # 调用get_file_path获取文件和文件夹名方法
file_dir.delete_file(del_file_lists, needfile_lists)  # 调用delete_file删除文件
file_dir.delete_dir(del_dir_lists, needdir_list)  # 调用delete_dir删除文件夹方法
