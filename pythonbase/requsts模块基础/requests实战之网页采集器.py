import requests

#UA: User-Agent (请求身载体的身份标识)
#反爬策略：UA检测  防反爬策略：UA伪装

#UA检测：门户网站的服务器会检测对应请求的载体身份标识，如果检测到请求的载体身份标识为某一款浏览器，
#说明该请求是一个正确的浏览器请求。但是，如果检测到请求的窄体身份标识不是某一款浏览器，则表示该请求为不正常的的请求（爬虫）
#则服务器可能拒绝该次请求

#UA伪装：让爬虫对应的请求载体身份标识伪装成某一款浏览器


if __name__ == '__main__':
    #UA伪装：将对应的User-Agent封装到一个字典中
    headers ={
        'User-Agent':'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'
    }

    # 1 URL = 'https://www.sogou.com/web?query=%E5%B0%8F%E7%BA%A2'  #中文被编码，也可以用中文
    URL = 'https://www.sogou.com/web'
    #处理URL携带的参数： 封装到字典中
    kw = input('enter a word:')
    param = {
        'query':kw
    }
    #对指定的url发起的请求对应的url是携带参数的，并且请求过程中处理了参数
    response = requests.get(url=URL,params=param,headers=headers)

    page_text= response.text
    fileName = kw+'.html'
    with open(fileName,'w',encoding='utf-8') as fp:
        fp.write(page_text)
    print(fileName,'保存成功！！！')