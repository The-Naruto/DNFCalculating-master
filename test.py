# -*- coding: utf-8 -*-
# @Time    : 2021/1/29 9:20
# @Author  : Naruto
# @Email   : the-naruto@foxmail.com
# @Project : DNFCalculating-master

import json
import os


def replaceStr(str):
    return str.replace('(', '1').replace(')', '2')

def recoverStr(str):
    return str.replace('1', '(').replace('2', ')')

print(replaceStr('aaa(dd)'))
print(recoverStr('aaa(dd)'))

# a1b2 = 111
# print(a1b2)


# # lambda state, index = 角色列表[i]: self.职业版本判断(index)
# if not os.path.exists('./ResourceFiles'):
#     print( "解压错误", "未找到资源文件，请将压缩包中ResourceFiles解压到同目录后打开计算器")
#
# with open("ResourceFiles/Config/adventure_info.json", encoding='utf-8') as fp:
#     角色列表 = json.load(fp)
#     print(角色列表)