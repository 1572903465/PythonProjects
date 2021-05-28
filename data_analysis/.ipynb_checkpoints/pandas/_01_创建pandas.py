import pandas as pd


"""创建Series带标签数组（索引）,未创建索引则自建索引"""
p1 = pd.Series([1,21,31,12,3,4])
print(p1)

"""指定索引"""
p2 = pd.Series([1,23,2,45,6],index=list("ABCDE")) # list()将字符串转换成列表

print(p2)

"""用字典创建Series,key->索引，value->值"""
temp_dict = {
    "name":"xiaoming",
    "age":16,
    "tel":10010
}
p3 = pd.Series(temp_dict)
print(p3)

"""切片索引"""
print("切片索引")
print(p3[1:2:2])
print(p2[1:5:2])

"""切片索引"""
print("直接索引")
print(p3[["name","age"]])
print(p3["name"])

"""布尔索引"""
print("布尔索引")

print(p2[p2>4])

"""读取全部的index和值"""
print("读取全部的index和值")
print(p3.index)
print(p3.values)