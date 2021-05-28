import json

data = {
    "students": [
        { "name":"北山啦" , "age":20 },
        { "name":"张三" , "age":30 },
        { "name":"里斯" , "age":17 }
    ]
}
print(type(data))
print(data["students"][0])
json_str = json.dumps(data)
print(type(json_str))
