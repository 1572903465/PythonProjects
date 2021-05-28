import requests
import json

if __name__ == '__main__':
    # UA伪装
    headers = {
        'User-Agent': 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'
    }
    url='http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword';
    params = {
        'cname':'',
        'pid':'',
        'keyword': '北京',
        'pageIndex': '2',
        'pageSize': '10',
    }
    response = requests.post(url=url,params=params,headers=headers)
    page_text = response.text
    with open('.kfc.txt','w',encoding='utf-8') as fp:
        fp.write(page_text)
    print(page_text)

