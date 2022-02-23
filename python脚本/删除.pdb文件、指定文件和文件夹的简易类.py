import os
import shutil


def load_file():
    """获取当前文件的父目录"""
    current_path = os.path.abspath(__file__)  # 获取当前文件路径
    father_path = os.path.abspath(os.path.dirname(current_path) + os.path.sep + ".")  # 获取当前文件的父目录
    return father_path


class DeleteFileDir:
    """直接删除文件和文件夹的简易类"""
    def __init__(self, root_path, files_or_dir=[], del_file=[], del_dir=[]):
        """初始化"""
        self.root_path = root_path  # 目录
        self.files_or_dir = files_or_dir  # 文件或文件夹
        self.del_file = del_file  # 删除的文件
        self.del_dir = del_dir  # 删除的文件夹

    def get_file_dir(self):
        """获取文件和文件夹名的方法"""
        self.files_or_dir = os.listdir(self.root_path)
        return self.files_or_dir

    def delete_file_dir(self, del_file_lists, del_dir_lists):
        """删除指定文件和文件夹的方法"""
        for file_name in self.files_or_dir:
            if file_name.endswith('.pdb'):  # 删除以.pdb结尾的文件
                os.remove(file_name)
            elif file_name in del_file_lists:  # 删除指定文件
                self.del_file.append(file_name)
                os.remove(file_name)
            elif file_name in del_dir_lists:  # 删除指定文件夹
                self.del_dir.append(file_name)
                shutil.rmtree(file_name, True)
        print("已删除的文件：{}".format(self.del_file))
        print("已删除的文件夹：{}".format(self.del_dir))


del_file_list = ['1.txt', '2.txt']  # 指定要删除的文件名称
del_dir_list = ['1', '2']  # 指定要删除的文件夹名称

root_path = load_file()  # 获取当前文件的父目录并赋值
file_dir = DeleteFileDir(root_path)  # 调用DeleteFileDir类
file_dir.get_file_dir()  # 调用get_file_dir获取文件和文件夹名方法
file_dir.delete_file_dir(del_file_list, del_dir_list)  # 调用delete_file_dir删除文件和文件夹