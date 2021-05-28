import pandas as pd
import numpy as np

"""创建dataFrame,dataframe 对象既有行索引，又有列索引"""
# 行索引，表明不同行，横向索引，叫index，0轴，axis=0
# 列索引，表名不同列，纵向索引，叫columns，1轴，axis=1
p1 = pd.DataFrame(np.arange(12).reshape(3,4))
print(p1)

p2 = pd.DataFrame(np.arange(12).reshape(3,4),index=list("abc"),columns=list("WXYZ"))
print(p2)

"通过字典创建dataframe"
d1 = {
    "name":["xiaoming","xiaogang"],
    "age":[20,32],
    "tel":[10010,10000]
}

p3 = pd.DataFrame(d1)
print(p3)
d2 = [{"name":"xiaoming","age":16,"tel":10010},{"name":"xiaogang","tel":10011},{"name":"xiaowang","age":23}]
p4 = pd.DataFrame(d2)
print(p4)

