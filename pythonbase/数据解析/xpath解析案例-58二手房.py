import requests
from  lxml import etree
if __name__ == '__main__':
    # 爬取页面源码数据
    url = 'https://cd.58.com/ershoufang/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'
    }
    page_text = requests.get(url=url,headers=headers).text
    # print(page_text)

    #数据解析
    tree  = etree.HTML(page_text)
    # 储存的就是li标签对象
    li_list=tree.xpath('//ul[@class="house-list-wrap"]/li')
    print(li_list)
    fp = open('../requsts模块基础/58.txt', 'w', encoding='utf-8')
    for li in li_list:
        #局部解析
        title = li.xpath('./div[@class="list-info"]/h2/a/text()')[0]
        print(title)
        fp.write(title+'\n')
