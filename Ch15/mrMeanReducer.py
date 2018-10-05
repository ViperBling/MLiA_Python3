# coding:utf-8

import sys
import numpy as np

'''
    mapper 接受原始的输入并产生中间值传递给 reducer。
    很多的mapper是并行执行的，所以需要将这些mapper的输出合并成一个值。
    即：将中间的 key/value 对进行组合。
'''

def read_input(file):
    for line in file:
        yield line.rstrip()


input = read_input(sys.stdin)                     # 接受mrMeanMapper的输出作为输入
mapperOut = [line.split('\t') for line in input]  # 将输入分割成单独的一个列表存储在大列表中
print(mapperOut)
cumVal = 0.0                                      # 样本总和，均值×样本量
cumSumSq = 0.0                                    # 样本平方总和，平方均值×样本量
cumN = 0.0                                        # 输入到这个reducer中的样本总量
for instance in mapperOut:
    nj = float(instance[0])                       # nj : 一个mapper中的样本数量
    cumN += nj
    cumVal += nj * float(instance[1])
    cumSumSq += nj * float(instance[2])
mean = cumVal / cumN                              # 总均值
varSum = (cumSumSq - 2 * mean * cumVal + cumN * mean * mean) / cumN   # 总方差

print("%d\t%f\t%f" % (cumN, mean, varSum))
print("reduce report: still alive", file=sys.stderr)