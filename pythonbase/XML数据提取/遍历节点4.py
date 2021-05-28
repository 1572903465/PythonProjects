# coding:utf-8
import xml
import xml.etree.ElementTree as ET
import pandas as pd
"""
实现从xml文件中读取数据
"""
# 全局唯一标识
unique_id = 1
sequence_id = 0

# 遍历所有的节点
def walkData(root_node, parent_id, level, result_list):
    global unique_id
    temp_list = [unique_id, parent_id, level, root_node.tag]
    result_list.append(temp_list)
    parent_id = unique_id
    unique_id += 1
    # 遍历每个子节点
    children_node = root_node.getchildren()
    children_node1 = root_node.findall(root_node.tag)

    # print(root_node.tag,children_node1)
    if len(children_node) == 0:
        return
    for child in children_node:
        walkData(child, parent_id, level + 1, result_list)
    return

def create_element(root_node,count):
    element_list = []
    # print(count)
    while count > 0:
        count -= 1
        element_list.append(root_node.makeelement('*',{}))
    return element_list

# 生成新的序列
def generate_sequence(root_node,level, childrens_list,children_dict,child_count):
    global sequence_id

    # 遍历每个子节点
    sequence_id +=1
    ment = root_node.makeelement('*',{})
    # print(type(root_node),ment)
    children_node = root_node.getchildren()
    if root_node.tag == '*':
        temp_list = [0, root_node.tag]
    else:
        temp_list = [len(children_node), root_node.tag]
    childrens_list.append(temp_list)
    # for i in children_node:
    #     print(root_node,i,level)
    # print(root_node,len(children_node),level,children_dict[level+1])
    if len(children_node) < children_dict[level+1]:
        element_list = create_element(root_node,children_dict[level+1]-len(children_node))
        root_node.extend(element_list)
        children_node = root_node.getchildren()
    print(sequence_id,root_node, len(children_node), level, children_dict[level + 1],len(children_dict)-2)
    if level < len(children_dict)-2:
        for child in children_node:
            generate_sequence(child, level + 1, childrens_list,children_dict,len(children_node))
    return


def getXmlData(file_name):
    level = 1  # 节点的深度从1开始
    result_list = []
    root = ET.parse(file_name).getroot()
    walkData(root, 0,level, result_list)
    return result_list

def getXMlSequence(file_name,children_dict):
    level = 1  # 节点的深度从1开始
    childrens_list = []
    root = ET.parse(file_name).getroot()
    # children_dict ={
    #     1: 1,
    #     2: 3,
    #     3: 3,
    #     4: 2,
    #     5: 0
    # }
    children_dict[len()]
    generate_sequence(root, level, childrens_list, children_dict,3)
    return childrens_list

def get_parent_childrens_count(file_name):
    # 'd:\\fenlei2.xml'
    # file_name = './a.xml'
    R = getXmlData(file_name)
    df = pd.DataFrame(R,columns=["NO.","parent","level","name"])
    # df.merge(df1)
    grouped = df.groupby(by="parent")
    # print(grouped)
    # for i,j in grouped:
    #     print(i)
    #     print(j)
    #     print("-"*100)
    # print(df)
    # print("*" * 100)
    # print(grouped[["parent","level"]].count())
    # print("*"*100)
    # print(grouped.count(),type(grouped.count()))
    # print(list(grouped.count().index))
    parent_childrens_count = []
    for i in list(grouped.count().index): # i是parent
        # print(df[df["parent"] == i])
        # print(i,df[df["parent"] == i].iloc[0,2],df[df["parent"] == i].shape[0]) # parent,level,chindrens
        parent_childrens_count.append([i,df[df["parent"] == i].iloc[0,2],df[df["parent"] == i].shape[0]])
    # print(parent_childrens_count)
    childrens_count = {}
    for i in parent_childrens_count:
        if i[1] in childrens_count:
            if childrens_count[i[1]] < i[2]:
                childrens_count[i[1]] = i[2]
        else:
            childrens_count[i[1]] = i[2]

    # print(childrens_count)
    return parent_childrens_count
    # u = df["level"].unique() # 返回NumPy数组ndarray中唯一元素值的列表
    # print(u)
    # print(type(u))
    # vc = df["level"].value_counts()
    # print(vc)
    # print(type(vc))
    # print(df.iloc[:,[1,2]])
    # for x in R:
    #     print(x)
    #     pass

def xml_similarity_count():
    # 'd:\\fenlei2.xml'
    file_name = './a.xml'
    parent_childrens_count = get_parent_childrens_count(file_name)
    print(parent_childrens_count)
    childrens_count = {}
    for i in parent_childrens_count:
        if i[1] in childrens_count:
            if childrens_count[i[1]] < i[2]:
                childrens_count[i[1]] = i[2]
        else:
            childrens_count[i[1]] = i[2]
    file_name = './b.xml'
    parent_childrens_count = get_parent_childrens_count(file_name)
    for i in parent_childrens_count:
        if i[1] in childrens_count:
            if childrens_count[i[1]] < i[2]:
                childrens_count[i[1]] = i[2]
        else:
            childrens_count[i[1]] = i[2]
        if i[1] + 1 not in childrens_count:
            childrens_count[i[1] + 1] = 0
    print(childrens_count)
    children_list = get_parent_childrens_count(file_name,childrens_count)
    for x in children_list:
        print(x)
        pass



if __name__ == '__main__':
    # 'd:\\fenlei2.xml'
    file_name = './a.xml'
    # R = getXmlData(file_name)
    # for x in R:
    #     print(x)
    #     pass
    xml_similarity_count()
    d = {}
    # children_list = getXMlSequence(file_name,d)
    # for x in children_list:
    #     print(x)
    #     pass