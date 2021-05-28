import json

data = {
    "students": [
        { "name":"北山啦" , "age":20 },
        { "name":"张三" , "age":30 },
        { "name":"里斯" , "age":17 }
    ]
}
with open("students.txt","w",encoding='utf-8') as fp:
    json.dump(data, fp, ensure_ascii=False)
    print("finish")
