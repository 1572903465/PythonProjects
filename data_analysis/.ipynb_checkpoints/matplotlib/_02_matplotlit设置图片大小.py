from matplotlib import pyplot as plt

fig = plt.figure(figsize=(16,15),dpi = 80)
# figure图像图标的意思，在这里指的就是我们画的图
# 通过实例化一个figure并且传递参数，能够在后台自动使用该figure实例
# 在图像模糊的时候可以传入dpi参数，让图片更加清晰


x = range(2,26,2)
# 数据在x轴的位置，是一个可迭代对象

y = [15,13,14.5,17,20,25,26,26,24,22,18,15]
# 数据在y轴的位置，是一个可迭代对象
# x轴和y轴的数据一起组成了所有要绘制出的坐标

plt.plot(x,y)  # 传入x和y，通过plot绘制出折线图

plt.savefig("./sig_size.png")
# 保存图片

plt.show()   # 在执行程序的时候展示图形


