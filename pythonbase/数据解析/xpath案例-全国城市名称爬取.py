import requests
from lxml import etree
if __name__ == '__main__':
    url='https://www.aqistudy.cn/historydata/'
    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'
    # }
    # page_test = requests.get(url=url,headers=headers).text
    # tree = etree.HTML(page_test)
    # hot_li_list=tree.xpath('//div[@class="bottom"]/ul/li')
    # all_city_names = []
    # for li in hot_li_list:
    #     hot_city_name = li.xpath('./a/text()')[0]
    #     all_city_names.append(hot_city_name)
    #     print(hot_city_name)
    # all_city_list=tree.xpath('//div[@class="bottom"]/ul/div[2]/li')
    # for li in all_city_list:
    #     city_name = li.xpath('./a/text()')[0]
    #     print(city_name)
    #     all_city_names.append(city_name)
    url='https://www.aqistudy.cn/historydata/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'
    }
    page_test = requests.get(url=url,headers=headers).text
    tree = etree.HTML(page_test)
    #解析到热门城市和所有城市对应的a标签
    a_list = tree.xpath('//div[@class="bottom"]/ul/li | //div[@class="bottom"]/ul/div[2]/li')
    all_city_names = []
    for li in a_list:
        hot_city_name = li.xpath('./a/text()')[0]
        all_city_names.append(hot_city_name)
    print(all_city_names,len(all_city_names))