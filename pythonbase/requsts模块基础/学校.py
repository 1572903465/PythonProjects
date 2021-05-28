import requests
import json
from lxml import etree

if __name__ == '__main__':
    # UA伪装
    headers = {
        'User-Agent': 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'
    }
    url='http://202.115.194.60/(S(1mkbggfiabevervowgid0zkx))/default.aspx'
    response = requests.post(url=url,headers=headers)
    page_text = response.text
    tree = etree.HTML(page_text)
    img_src = 'http://202.115.194.60/(S(1mkbggfiabevervowgid0zkx))/'+tree.xpath('//*[@id="imgCode"]/@src')[0]
    print(img_src)
    img_data = requests.get(url=img_src,headers=headers).content
    print(img_data)
    with open('./code.jpg', 'wb') as fp:
        fp.write(img_data)
    with open('.kfc.txt','w',encoding='utf-8') as fp:
        fp.write(page_text)
    # print(page_text)
    login_url = 'http://202.115.194.60/(S(a0kih41z5k44kopfqcwl55pr))/ Default.aspx'

