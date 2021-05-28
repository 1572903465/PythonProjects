import requests
if __name__ == '__main__':
    url = 'https://tieba.baidu.com/p/6156634738'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'
    }
    params = {
        'pn':'1'
    }
    page_text = requests.get(url=url,headers=headers,params=params).text
    print(page_text)