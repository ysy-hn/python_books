import os
import shutil


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

    def delete_file(self, del_file_lists):
        """删除文件方法"""
        for file_name in self.file_list:
            if file_name in del_file_lists:
                self.del_file.append(file_name)
                os.remove(file_name)
        print("已删除的文件：{}".format(self.del_file))

    def delete_dir(self, del_dir_lists):
        """删除文件夹方法"""
        for dir_name in self.dir_list:
            if dir_name in del_dir_lists:
                self.del_dir.append(dir_name)
                shutil.rmtree(dir_name, True)
        print("已删除的文件夹：{}".format(self.del_dir))


file_list = []
dir_list = []
root = os.getcwd()  # 返回当前工作目录
root_path = path_name(root)  # 将同一级别的其它目录赋值给root_path

file_dir = DeleteFileDir(root_path, file_list, dir_list, del_file=[], del_dir=[])

del_file_list = ['3.txt', '2.txt']  # 指定要删除的文件名称
del_dir_list = ['1', '4']  # 指定要删除的文件夹名称
del_file_lists = [root_path + x for x in del_file_list]
del_dir_lists = [root_path + x for x in del_dir_list]

file_dir.get_file_path()  # 调用get_file_path获取文件和文件夹名方法
file_dir.delete_file(del_file_lists)  # 调用delete_file删除文件
file_dir.delete_dir(del_dir_lists)  # 调用delete_dir删除文件夹方法
