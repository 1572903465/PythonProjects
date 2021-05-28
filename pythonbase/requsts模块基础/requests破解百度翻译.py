import requests
import json

if __name__ == '__main__':

    URL ='https://fanyi.baidu.com/sug'
    # UA伪装：将对应的User-Agent封装到一个字典中
    headers = {
        'User-Agent': 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'
    }
    data = {
        'kw':'cat'
    }
    data['kw']='dog'
    response = requests.post(url=URL,data=data,headers=headers)
    #json()方法返回的是obj(如果确认响应数据是json类型的，才可以使用json方法() )
    dic_obj = response.json()
    print(dic_obj)
    #持久化存储
    fp =open('./dog.json','w',encoding='utf-8')
    json.dump(dic_obj,fp=fp,ensure_ascii=False)