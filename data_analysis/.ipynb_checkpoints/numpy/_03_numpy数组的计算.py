import numpy as np


t5=np.arange(24).reshape((2,3,4))

t5 = t5.reshape(4,6)
print(t5)
""" nupmy 数组的计算具有广播效应,数组和数字计算"""
print(t5 + 2)
print(t5 * 2)
print(t5 / 2)
# print(t5 / 0)

"""numpy相同形状数组进行计算 对应位置的进行计算"""
t6 = np.arange(100,124).reshape((4,6))
print(t6)
print(t5+t6)
print(t5*t6)

"""维度相同进行计算"""
t7 = np.arange(0,6)
print(t5-t7)

t8 = np.arange(4).reshape((4,1))
print(t5-t8)



