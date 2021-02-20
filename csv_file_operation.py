# -*- coding: utf-8 -*-
# @Time    : 2021/2/3 8:41
# @Author  : Naruto
# @Email   : the-naruto@foxmail.com
# @Project : DNFCalculating-master

import os
import csv
from datetime import datetime

Path = '数据记录'

def get_csvfile(path):
    file_list = os.listdir(path)
    if len(file_list)==0:
        return []
#     筛选掉非csv的文件
    new_file = []
    for f in file_list:
        if ".csv" in f and "·" in f:
            new_file.append(f)
    # 增加路径
    dir_file = []
    for f in new_file:
        dir_file.append(os.path.join(path,f))
    print(os.path.abspath(dir_file[0]))
    return dir_file


def merge_csvfile(path,dir_file):
    now = datetime.now()
    if len(dir_file) < 1:
        return
    arr = []
    for file_path in dir_file:
        # print(file_path)
        reader = csv.reader(open(file_path))
        for line in reader:
            print(line[12])
            line.append(file_path.split('-')[0].split('\\')[1])
            arr.append(line)
            #
            break
    # print(arr)
    arr  = bubble_sort(arr)
    filename = os.path.join(path,'已选职业伤害榜')+now.strftime('%Y-%m-%d-%H-%M-%S')+'.csv'
    with open(filename, "w") as f:
        for a in arr:
            f.write(','.join(l for l in a) + '\n')

    # 删除旧的每个文件
    if os.path.exists(filename):
        for path in dir_file:
            os.remove(os.path.abspath(path))

def bubble_sort(arr):
    #冒泡排序
    # 第一层for表示循环的遍数
    for i in range(len(arr) - 1):
        # 第二层for表示具体比较哪两个元素
        for j in range(len(arr) - 1 - i):
            if float(arr[j][12]) < float(arr[j + 1][12]):
                # 如果前面的小于后面的，则交换这两个元素的位置
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    print([a[12] for a in arr])
    return arr


def get_file_and_merge(path):
    file_paths = get_csvfile(path)
    merge_csvfile(file_paths)


#
# dir_file = get_csvfile(Path)
# a = merge_csvfile(Path,dir_file)

#
#
# with open(dir_file[0],"r") as csvfile:
#     reader = csv.reader(csvfile)
#     #这里不需要readlines
#     for line in reader:
#         print(line)




