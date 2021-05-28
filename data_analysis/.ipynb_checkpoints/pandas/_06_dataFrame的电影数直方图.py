import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

df =pd.read_csv("./datasets_IMDB-Movie-Data.csv")
print(df.info())

print(df.head(1))

# rating runtime分布情况
# 选择图形
# 准备数据
runtime_data = df["Runtime (Minutes)"].values


max_runtime = runtime_data.max()
min_runtime = runtime_data.min()

# 计算组数
num_bin = (max_runtime-min_runtime)//5

# 设置图像的大小
# plt.figure(figsize=(20,8),dpi = 80)
plt.hist(runtime_data,num_bin)

plt.xticks(range(min_runtime,max_runtime+5,5))

plt.show()