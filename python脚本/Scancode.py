# coding=utf-8
"""
输入一个字符串，固定长25
例：172H07763E8235101803038096
分割：172H07763E 82351018 03 038 096
"""


class TScanCodeInfo:
    def __init__(self):
        self.JobName = ''
        self.BatchNo = ''
        self.LayerName = ''
        self.PanelThickness = '0'
        self.BatchCount = '0'
        self.IsSucc = 'True'
        self.message = ''

def data_space(ScanCodeStr):
    result = TScanCodeInfo()
    if len(ScanCodeStr) == 26:
        result.JobName = ScanCodeStr[0:10]
        result.BatchNo = ScanCodeStr[10:18]
        result.LayerName = ScanCodeStr[18:20]
        if ScanCodeStr[20:23].isdigit():
            result.PanelThickness = float(ScanCodeStr[20:23])
        else:
            result.message = 'PanelThickness：{}，错误，请输入数字'.format(ScanCodeStr[20:23])
        if ScanCodeStr[23:].isdigit():
            result.BatchCount = int(ScanCodeStr[23:])
        else:
            result.message = 'BatchCount：{}，错误，请输入数字'.format(ScanCodeStr[23:])
    else:
        result.IsSucc = 'False'
        result.message = "输入的数据异常：长度为{}，请重新输入！".format(len(ScanCodeStr))
    return result


p1 = {'ScanCodeStr': '172H07763E82351018030l8096'}
_result_ = data_space(p1.get("ScanCodeStr"))
print(_result_.JobName, _result_.IsSucc, _result_.message)
