# coding=utf-8
import pandas as pd
import numpy as np

file_path = "./starbucks_store_worldwide.csv"

df = pd.read_csv(file_path)
pd.set_option("display.max_columns",None)  # 输出显示最大列数树 None 默认最大 100 显示100列

# print(df.head(1))
# print(df.info())
# grouped = df.groupby(by="Country")
# print(grouped)

#DataFrameGroupBy
#可以进行遍历
# for i,j in grouped:
#     print(i)
#     print("-"*100)
#     print(j,type(j))
#     print("*"*100)
# df[df["Country"]="US"]
#调用聚合方法


# country_count = grouped["Brand"].count()
# print(country_count["US"])
# print(country_count["CN"])

#统计中国每个省店铺的数量
# china_data = df[df["Country"] =="CN"]  # df["Country"] =="CN" 布尔索引 Country  是 CN 就是 ture 否则就是false
# print(df["Country"]=="CN")
#
# grouped = china_data.groupby(by="State/Province").count()["Brand"]
#
# print(grouped)

#数据按照多个条件进行分组,返回Series
# grouped = df["Brand"].groupby(by=[df["Country"],df["State/Province"]]).count()
# print(grouped)
# print(type(grouped))

#数据按照多个条件进行分组,返回DataFrame
grouped1 = df[["Brand"]].groupby(by=[df["Country"],df["State/Province"]]).count()
# grouped2= df.groupby(by=[df["Country"],df["State/Province"]])[["Brand"]].count()
# grouped3 = df.groupby(by=[df["Country"],df["State/Province"]]).count()[["Brand"]]
print(df["Brand"])
print('*'*100)
print([df["Country"],df["State/Province"]])
# print(grouped1,type(grouped1))
# print("*"*100)
# print(grouped2,type(grouped2))
# print("*"*100)
#
# print(grouped3,type(grouped3))

#索引的方法和属性
print(grouped1.index)
