from matplotlib import pyplot as plt

x = range(2,26,2)
# 数据在x轴的位置，是一个可迭代对象

y = [15,13,14.5,17,20,25,26,26,24,22,18,15]
# 数据在y轴的位置，是一个可迭代对象
# x轴和y轴的数据一起组成了所有要绘制出的坐标

plt.plot(x,y)  # 传入x和y，通过plot绘制出折线图
plt.show()   # 在执行程序的时候展示图形


