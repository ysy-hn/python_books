w0 = '对准相机查看PANEL'
w1 = '中心坐标'
w2 = 'PANEL'
a = []
c = ['32','48','60','66']
# with open('data.txt', 'r') as f:
#     lines = f.readlines()
#     for line in lines:
#         if line[39] == "L":
#             if line[41] == '区':
#                 b = "{}".format(line[40])
#             else:
#                 b = "{}{}".format(line[40], line[41])
#             a.append(b)
# c = set(a)
for d in c:
    with open('data.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            if w0 in line and (line[49] + line[50] == d):
                if line[53] == '1':
                    if line[59] == '3':
                        C1A3 = "{}".format(line[80:])
                    elif line[59] == '4':
                        C1A4 = "{}".format(line[80:])
                elif line[53] == '2':
                    if line[59] == '1':
                        C2A1 = "{}".format(line[80:])
                    elif line[59] == '2':
                        C2A2 = "{}".format(line[80:])
                elif line[53] == '0':
                    if line[59] == '1':
                        C1A2 = "{}".format(line[80:])
                    elif line[59] == '3':
                        C1A1 = "{}{} {}".format(line[49], line[50], line[80:])
                    elif line[59] == '2':
                        C2A3 = "{}".format(line[80:])
                    elif line[59] == '4':
                        C2A4 = "{}".format(line[80:])
            elif w1 in line and (line[40] + line[41] == d):
                if line[44] == '1':
                    if line[46] == '1':
                        R1K1 = "{}".format(line[59:])
                    elif line[46] == '2':
                        R1K2 = "{}".format(line[59:])
                    elif line[46] == '3':
                        R1K3 = "{}".format(line[59:])
                    elif line[46] == '4':
                        R1K4 = "{}".format(line[59:])
                elif line[44] == '2':
                    if line[46] == '1':
                        R2K1 = "{}".format(line[59:])
                    elif line[46] == '2':
                        R2K2 = "{}".format(line[59:])
                    elif line[46] == '3':
                        R2K3 = "{}".format(line[59:])
                    elif line[46] == '4':
                        R2K4 = "{}".format(line[59:])
        # e = [C1A1, C1A2, C1A3, C1A4, C2A1, C2A2, C2A3, C2A4, R1K1, R1K2, R1K3, R1K4, R2K1, R2K2, R2K3, R2K4, '\n']
        e = [C1A1.strip("\n"), '******', R1K1,
             C1A2.strip("\n"), '******', R1K2,
             C1A3.strip("\n"), '******', R1K3,
             C1A4.strip("\n"), '******', R1K4,
             C2A1.strip("\n"), '******', R2K1,
             C2A2.strip("\n"), '******', R2K2,
             C2A3.strip("\n"), '******', R2K3,
             C2A4.strip("\n"), '******', R2K4,
             '\n']
        with open('3.txt', 'a') as f:
            for g in e:
                f.write(g)

#
#
# import re
#
# w0 = '中心坐标'
# w1 = 'CAM'
# w2 = 'PANEL'
# w3 = '区域'
# w4 = '靶标'
#
#
# with open('data.txt', 'r') as f:
#     lines = f.readlines()
#     for line in lines:
#         if w0 in line:
#             if w2 in line:
#                 a = line[line.index(w2) + len(w2)] + line[line.index(w2) + len(w2) +1]
#                 b = line[line.index(w3) + len(w3)]
#                 c = line[line.index(w4) - len(w4)]
#             print(a, b, c)
#             e = re.findall(r'[0-9]+\.[0-9]+', line)
#             print(e)
