
#!/usr/bin/python3
# -*- coding: UTF-8 -*-

'''
版本迭代
1、多次运行时，保证只有单组数字
2、数字为多位时的处理
3、运行时自动读取当前文件夹的路径
4、添加自动处理子文件夹下的文件
'''

import os

def rename_file(path):
    # 读取路径下的所有的文件
    files = os.listdir(path)
    file_num = 0
    # 遍历文件夹下所有的文件
    for name in files:
        # 需要加上绝对路径-否则会把文件夹识别为文件
        name_path = path + "\\" + name
        # 跳过本文件
        if name == "auto_make_name.py":
            continue

        # 判断是否为文件: true为文件-false为文件夹
        if os.path.isfile(name_path) == True:
            # print("file:", name)
            file_num = file_num + 1
            filter = ""
            # 判断首字母是否为数字
            if name[0].isdigit() == True:
                num_cnt = 0
                # 循环遍历文件名称
                for c in name:
                    if c.isdigit() == True:
                        num_cnt = num_cnt + 1
                    else:
                        break
                # 加上-号的位置
                num_cnt = num_cnt + 1
                filter = name[num_cnt:]
            else:
                # print("字母:", name)
                filter = name

            new_name = str(file_num) + "-" + filter
            print("new_name:", new_name)

            # 此处需要加上文件的绝对路径（之前是使用相对路径，但是在子文件的时候容易会出错）
            new_name = path + "\\" + new_name
            os.rename(name_path, new_name)
        else:
            # print("dirc:", name)
            # 处理文件夹
            sub_path = path + "\\" + name
            print("sub_path:", sub_path)
            rename_file(sub_path)

if __name__ == '__main__':
    # 获取当前工作路径
    path = os.getcwd()
    print("path:", path)

    # 改名字
    rename_file(path)


