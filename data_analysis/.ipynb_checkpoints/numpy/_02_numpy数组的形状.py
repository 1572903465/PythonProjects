import numpy as np

"""查看数组的形状 np.shape"""
# numpy 一维数组
t1 = np.arange(12)
print(t1)
print(t1.shape)

# numpy 二维数组
t2 = np.array([[1,2,3],[4,5,6]])
print(t2)
print(t2.shape)


""" 修改数组的形状 np.reshape((x,y)) ,不会对原数组产生影响"""
t4 = np.arange(12)
print(t4)
t4.reshape((3,4))
print(t4.reshape((3,4)))

t5=np.arange(24).reshape((2,3,4))
print(t5)

#  flatten()  数据展开成一维
print(t5.flatten())

