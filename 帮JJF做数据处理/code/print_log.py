"""
文件说明：
    功能：
        1、打印元数据、支持度、置信度
"""
import head

def print_support(list):
    f = open(head.path_support, 'wt')

    for k,v in list.items():
        print(k,v, file=f)

def print_confidence(list):
    f = open(head.path_confidence, 'wt')

    for i in list:
        print(i, file=f)

def print_source(list):
    f = open(head.path_source, 'wt')

    for i in list:
        print(i, file=f)