import pandas as pd
import numpy as np


df =pd.read_csv("./datasets_IMDB-Movie-Data.csv")
pd.set_option("display.max_columns",None)  # 输出显示最大列数树 None 默认最大 100 显示100列
print(df.info())

print(df.head(1))

# 获取平均评分
print(df["Rating"].mean())

# set()去重复
print(len(set(df["Director"].tolist())))
print(len(df["Director"].unique()))

# 获取演员的人数
temp_actors_list = df["Actors"].str.split(",").tolist()
# 双重列表 列表推导式
actors_list = [i for j in temp_actors_list for i in j]
# actors_list = list(np.array(temp_actors_list).flatten())

actors_num = len(set(actors_list))

print(actors_num)