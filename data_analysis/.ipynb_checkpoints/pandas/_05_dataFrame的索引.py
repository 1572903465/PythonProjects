import pandas as pd
import numpy as np


df =pd.read_csv("./dogNames2.csv")
df = df.sort_values(by="Count_AnimalName",ascending=False)

"""取行或者列的注意事项"""
"""- 方括号写数字，表示取行，对行进行操作"""
"""- 方括号写字符串，表示的是列索引，对列进行操作"""
print(df[:20])
print(df[:20]["Row_Labels"])

p2 = pd.DataFrame(np.arange(12).reshape(3,4),index=list("abc"),columns=list("WXYZ"))
print(p2)

"""df.loc通过标签索引行数据"""
"""df.iloc通过位置索引行数据"""
# 取第a行第Z列
print(p2.loc["a","Z"])
# 取第a行
print(p2.loc["a"])
# 取第Z列
print(p2.loc[:,"Z"])

# 取第a行第Z行，取多行
print(p2.loc[["a","c"]])
# 取多行多列
print(p2.loc[["a","c"],["W","Z"]])

# 取第一行
print(p2.iloc[1,:])

# 取第二列
print(p2.iloc[:,2])

# 取第0，2行，1，2列
print(p2.iloc[[0,2],[2,1]])

# 取连续的多行多列
print(p2.iloc[1:,:2])
