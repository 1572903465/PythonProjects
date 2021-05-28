import requests
import json

def main():
    URL = 'https://fanyi.baidu.com/sug'
    # UA伪装：将对应的User-Agent封装到一个字典中
    headers = {
        'User-Agent': 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'
    }
    file = open(r'word.txt', 'r', encoding='utf-8')
    # ‪C:\Users\weiwei\Desktop\demo1.docx
    words = file.readlines()
    file.close()
    # print(words)
    traslates=[]
    i=0
    file = open(r'C:\Users\weiwei\Desktop\word\translate.txt', 'a+', encoding='utf-8')
    for word in words:
        # print(word)
        data = {
            'kw': word.split("\n")[0]
        }
        response = requests.post(url=URL, data=data, headers=headers)
        # json()方法返回的是obj(如果确认响应数据是json类型的，才可以使用json方法() )
        dic_obj = response.json()
        with open("students.txt", "w", encoding='utf-8') as fp:
            json.dump(dic_obj, fp, ensure_ascii=False)
        with open("students.txt", encoding='utf-8') as fp:
            datas = json.load(fp)
            """取出字典key为students的数据，
            得到一个list，再从这个list中取第一个数据"""
            # print(datas['data'][0]['v'])
            if datas['data']:
                traslate = data['kw']+'\t\t'+datas['data'][0]['v']
        #     traslates.append(traslate)
                print(i)
                print(traslate)
                i+=1
                file.write(traslate + '\n')
            else:
                i += 1
                traslate = data['kw']
                file.write(traslate + '\n')
    file.close()
if __name__ == '__main__':
    main()



