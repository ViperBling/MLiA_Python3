# coding:utf-8

import sys
import numpy as np

'''
    这个mapper文件按行读取所有的输入，并创建一组对应的浮点值，得到一个numpy矩阵。
    再对所有的值平方，最后将均值和平方均值发送给reducer
'''


def read_input(file):
    for line in file:
        # 返回一个迭代器，不断获取下一个值，节省内存使用
        yield line.rstrip()

input = read_input(sys.stdin)            # 创建一个输入数据行的列表
input = [float(line) for line in input]  # 将得到的数据转化成float类型
numInputs = len(input)                   # 获取数据个数，即行数
input = np.mat(input)                    # 转化成Numpy矩阵
sqInput = np.power(input, 2)             # 对所有值平方

# 输出 数据的个数，n个数据的均值，n个数据平方之后的均值
# 第一行是标准输出，也就是reducer的输出
# 第二行识标准错误输出，即对主节点作出的响应报告，表明本节点工作正常。
print("%d\t%f\t%f" % (numInputs, np.mean(input), np.mean(sqInput)))
print("map report: still alive", file=sys.stderr)