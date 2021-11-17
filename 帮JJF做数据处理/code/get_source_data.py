"""
文件说明：
    功能：
        1、从相应的路径中获取源数据
        2、把源数据的标签映射到论文定义的标签
"""

import csv
import head

def get_2_co_occurrence():
    list_sum = []
    list_sum_u = get_data(head.input_path_u)
    list_sum_d = get_data(head.input_path_d)
    list_sum_g = get_data(head.input_path_g)
    list_sum_s = get_data(head.input_path_s)

    # list_sum = list_sum_u + list_sum_d + list_sum_g + list_sum_s
    if head.file_type == 'sum':
        list_sum = list_sum_u + list_sum_d + list_sum_g + list_sum_s
    elif head.file_type == 'g_s':
        list_sum = list_sum_g + list_sum_s
    elif head.file_type == 'u_d':
        list_sum = list_sum_u + list_sum_d
    else:
        list_sum = list_sum_u + list_sum_d + list_sum_g + list_sum_s

    print("get source data:")

    return list_sum

def get_data(input_path):
    temp_list = []
    knowledge_list = []
    with open(input_path, "r", encoding="utf8") as f:
        reader = csv.reader(f)
        for line in reader:
            knowledge_str = line[2]
            if knowledge_str == "knowledge":
                continue

            temp_list = []
            for k in knowledge_str.split(","):
                dest_val = map(k.strip())
                temp_list.append(dest_val)

            knowledge_list.append(temp_list)

    return knowledge_list

# 标签映射关系
def map(source_val):
    dest_val = ''
    try:
	    dest_val = head.dict_source[source_val]
    except:
        print("error:", source_val)

    return dest_val


