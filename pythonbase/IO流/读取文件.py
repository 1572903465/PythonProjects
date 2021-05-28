import json
with open("../英语单词爬虫/students.txt", encoding='utf-8') as fp:
    data = json.load(fp)
    """取出字典key为students的数据，
    得到一个list，再从这个list中取第一个数据"""
    print(data['data'][0])