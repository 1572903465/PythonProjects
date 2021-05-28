import requests
if __name__ == '__main__':
    url = 'https://www.baidu.com/s?wd=ip'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'
    }
    page_text = requests.get(url=url,headers=headers,proxies={"https":'113.194.151.79:9999'}).text
    with open('ip.html','w',encoding='utf-8') as fp:
        fp.write(page_text)