"""
文件说明：
    1、把confiden.txt文件中包含的置信度自动生成可视化Excel表格
"""

import print_log
import head
from xlwt import *
import xlwt
#需要xlwt库的支持

file = Workbook(encoding = 'utf-8')
#指定file以utf-8的格式打开

table = file.add_sheet('data')

max_num = 12
g_width = 4800
g_height = 20*40    #20为基准数，40意为40磅

def set_style(name, height, bold = False):
    style = xlwt.XFStyle()   #初始化样式

    alignment = xlwt.Alignment() #设置字体在单元格中的位置
    alignment.horz = xlwt.Alignment.HORZ_CENTER  #水平居左
    alignment.vert = xlwt.Alignment.VERT_CENTER  #垂直居中

    style.alignment = alignment

    return style

# 创建一个样式对象，初始化样式 style
style = xlwt.XFStyle()  

# 为样式创建字体
font = xlwt.Font()  
font.name = 'Calibri' # 设置字体
font.height = 300 # 字体大小

alignment = xlwt.Alignment() #设置字体在单元格中的位置
alignment.horz = xlwt.Alignment.HORZ_CENTER  #水平居左
alignment.vert = xlwt.Alignment.VERT_CENTER  #垂直居中
# alignment.horz = 1      # 设置水平位置，0是左对齐，1是居中，2是右对齐

# 定义格式-字体
style.font = font
style.alignment = alignment

def init_excel():
    table.col(0).width = g_width 
    table.row(0).height_mismatch = True
    table.row(0).height = g_height  

    for cnt in range(1, max_num):  
        table.col(cnt).width = g_width
        table.row(cnt).height_mismatch = True
        table.row(cnt).height = g_height

        table.write(cnt, 0, head.dict_num2char[cnt], style)
        table.write(0, cnt, head.dict_num2char[cnt], style)
        table.write(cnt, cnt, '\\', style)

def create_excel(line, row, c_val):
    line_idx = head.dict_char2num[line]
    row_idx = head.dict_char2num[row]
    temp = line_idx
    print(line_idx, row_idx, c_val, style)

    table.write(line_idx, row_idx, c_val, style)

def confidence_main():
    init_excel()

    f = open(head.path_confidence)
    lines = f.readlines()

    for line in lines:
        l = line.split(",")
        # 筛选两两之间的置信度
        if len(l) == 3:
            line = l[0][13:-3]		# 一行
            row = l[1][13:-3]		# 一列
            c_val = l[2][1:7]		# 前者对后者的置信度
            
            # 针对c_val过短的情况做特殊处理
            if len(l[2]) == 6:
                c_val = l[2][1:4]
                print("c_val6", c_val, l[2])
            elif len(l[2]) == 7:
                c_val = l[2][1:5]
                print("c_val7", c_val, l[2])
            elif len(l[2]) == 8:
                c_val = l[2][1:6]
                print("c_val8", c_val, l[2])

            create_excel(line, row, c_val)

    file.save(head.excel_suffix)



