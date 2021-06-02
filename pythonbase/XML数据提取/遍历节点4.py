# coding:utf-8
import xml
import xml.etree.ElementTree as ET
import pandas as pd
import os
import warnings
#  忽略DeprecationWarning
warnings.filterwarnings("ignore",category=DeprecationWarning)

"""
实现从xml文件中读取数据
"""
# 全局唯一标识
unique_id = 1
sequence_id = 0


# 获取文件夹下面的所有文件目录
# 输入文件夹名
# 输出文件夹下文件目录名列表
def all_path(dirname):
    path_list = []#所有的文件
    for maindir, subdir, file_name_list in os.walk(dirname):
        # print("1:",maindir) #当前主目录
        # print("2:",subdir) #当前主目录下的所有目录
        # print("3:",file_name_list)  #当前主目录下的所有文件
        for filename in file_name_list:
            path = os.path.join(maindir, filename)#合并成一个完整路径
            path_list.append(path)
    return path_list


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


# 创建一个空白节点列表
# 输入 节点名，节点数量
# 输出 子节点列表
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
    # print(sequence_id,root_node, len(children_node), level, children_dict[level + 1],len(children_dict)-2)
    if level < len(children_dict)-2:
        for child in children_node:
            generate_sequence(child, level + 1, childrens_list,children_dict,len(children_node))
    return


# 获取源树的序列
def getXmlData(file_name):
    level = 1  # 节点的深度从1开始
    result_list = []
    root = ET.parse(file_name).getroot()
    walkData(root, 0,level, result_list)
    return result_list


# 获取补码树去除叶子节点的深度遍历序列，和数值化序列
# 输入xml路径，补全字典
# 补全树深度遍历序列列表
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
    # print(children_dict)
    # children_dict[len(children_dict)] = 0
    generate_sequence(root, level, childrens_list, children_dict,3)
    return childrens_list

# 获取parent_childrens_count
# 输入文件路径
# 返回parent_childrens_count
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
        parent_childrens_count.append([i,df[df["parent"] == i].iloc[0,2],df[df["parent"] == i].shape[0]]) # parent,level,chindrens
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

def DL(index_seq_list,colums_seq_list):
    DL_result = 0
    for i in range(0, len(index_seq_list)):
        if index_seq_list[i] != colums_seq_list[i]:
            DL_result += 1
    # print(DL_result)
    return DL_result

# 获取源树和目标树相似度
def get_xml_similarity(index_path,columns_path,child_index,child_columns):
    # index_path = './a.xml'
    # columns_path = './b.xml'
    children_dict={}
    DS_result = 0
    # child_index = get_parent_childrens_count(index_path)
    # child_columns = get_parent_childrens_count(columns_path)
    # print(child_index, child_columns, index_path, columns_path)
    for i in child_index:
        if i[1] in children_dict:
            if children_dict[i[1]] < i[2]:
                children_dict[i[1]] = i[2]
        else:
            children_dict[i[1]] = i[2]
        if i[1] + 1 not in children_dict:
            children_dict[i[1] + 1] = 0

    for i in child_columns:
        if i[1] in children_dict:
            if children_dict[i[1]] < i[2]:
                children_dict[i[1]] = i[2]
        else:
            children_dict[i[1]] = i[2]
        if i[1] + 1 not in children_dict:
            children_dict[i[1] + 1] = 0
    # print(children_dict)
    index_list = getXMlSequence(index_path,children_dict)
    columns_list = getXMlSequence(columns_path, children_dict)
    # print(index_list)
    # print(columns_list)
    df_index = pd.DataFrame(index_list,columns=["value","node"])
    df_colums = pd.DataFrame(columns_list, columns=["value", "node"])
    if df_index["value"].max() >= df_colums["value"].max():
        max_count = df_index["value"].max()
    else:
        max_count = df_colums["value"].max()
    # print(max_count)
    index_list = list(df_index["value"])
    colums_list = list(df_colums['value'])
    index_seq_list  = list(df_index["node"])
    colums_seq_list = list(df_colums["node"])
    # print(index_list,colums_list)

    DL_result = DL(index_seq_list,colums_seq_list)
    index_str = ""
    colums_str = ""
    for i in index_list:
        for j in range(0, i):
            index_str += "1"
        for k in range(0, max_count - i):
            index_str += "0"
    for i in colums_list:
        for j in range(0, i):
            colums_str += "1"
        for k in range(0, max_count - i):
            colums_str += "0"
    # print(index_str,index_str)
    for i in range(0, len(index_str)):
        if index_str[i] != colums_str[i]:
            DS_result += 1
    Sim = 1-(DS_result+DL_result)*0.1/len(index_str)
    return Sim

# 获取xml_相似度矩阵
def xml_similarity_count(folder_path):
    # 'd:\\fenlei2.xml'
    # folder_path = "../xmlDatas"
    file_name_index = all_path(folder_path)
    file_name_colums = [i for i in file_name_index]
    # print(file_name_index)
    # print(file_name_colums)
    index_colums_list = []
    similarity_list = []
    for index_path in file_name_index:
        Sim_list = []
        child_index = get_parent_childrens_count(index_path)
        index_str = index_path.split('\\')[-1]
        index_colums_list.append(index_str)
        for columns_path in file_name_colums:
            child_columns = get_parent_childrens_count(columns_path)
            # print(index_str)
            Sim = get_xml_similarity(index_path,columns_path,child_index,child_columns)
            # print(Sim)
            Sim_list.append(1-Sim)
        similarity_list.append(Sim_list)
    # print(index_colums_list)
    # print(similarity_list)
    df_similar = pd.DataFrame(similarity_list,index=index_colums_list,columns=index_colums_list)
    # print(df_similar)
    return df_similar

if __name__ == '__main__':
    # 'd:\\fenlei2.xml'
    # file_name = './a.xml'
    # R = getXmlData(file_name)
    # for x in R:
    #     print(x)
    #     pass
    folder_path = "../xmlDatas"
    df_similar = xml_similarity_count(folder_path)
    # children_list = getXMlSequence(file_name,d)
    # for x in children_list:
    #     print(x)
    #     pass
    print(df_similar)

    # get_xml_similarity()