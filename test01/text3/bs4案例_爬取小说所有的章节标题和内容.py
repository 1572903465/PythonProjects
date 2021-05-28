import requests
from bs4 import BeautifulSoup
if __name__ == '__main__':
    #对首页的数据进行爬取
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'
    }
    url = 'https://www.shicimingju.com/book/sanguoyanyi.html'
    page_text = requests.get(url=url, headers=headers).text
    # print(page_text)
    #在首页中解析出章节的标题和详情页的url
    #1.实例化BeatifulfulSoup对象，需要页面源码数据加载到该对象中
    soup = BeautifulSoup(page_text, 'lxml')
    #解析章节标题和详情页的url
    li_list = soup.select('.book-mulu > ul >li')
    print(soup.select('.book-mulu > ul >li'))
    fp = open('./sanguo.txt','w',encoding='utf-8')
    for li in li_list:
        title = li.a.string
        detail_url = 'https://www.shicimingju.com'+li.a['href']
        #对详情页发送请求
        detail_page_text=requests.get(url=detail_url,headers=headers,timeout=(3,7)).text
        # print(detail_page_text)
        #解析出详情页中相关的章节内容
        detail_soup = BeautifulSoup(detail_page_text,'lxml')
        div_tag = detail_soup.find('div',class_ = 'chapter_content')
        #解析到了章节的内容
        content = div_tag.text
        # print(content)
        fp.write(title+':'+content+'\n')
        print(title,'爬取成功！！！')
