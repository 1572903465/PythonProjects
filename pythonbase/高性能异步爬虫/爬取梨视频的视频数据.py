import random

import requests
from lxml import etree
import re
from multiprocessing.dummy import Pool
#原则：线程池处理的是阻塞且耗时的操作
def get_video_data(dic):
    data = {
        'contId': dic['contId'],
        'mrd': dic['mrd'],
    }
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36',
        'Referer': 'https://www.pearvideo.com/video_' + dic['contId']
    }
    video_url = 'https://www.pearvideo.com/videoStatus.jsp'
    data_mp4 = requests.get(url=dic['url'], headers=header, params=data).content
    print(data_mp4)
    with open(dic['name'], 'wb') as fp:
        fp.write(data_mp4)
        print(dic['name'], '下载完成')
if __name__ == '__main__':
    url='https://www.pearvideo.com/category_2'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'
    }

    page_text = requests.get(url=url,headers=headers).text
    # print(page_text)
    tree = etree.HTML(page_text)
    li_list = tree.xpath('//*[@id="listvideoListUl"]/li ')
    # print(li_list,len(li_list))
    urls = []
    for li in li_list:
        detail_url = 'https://www.pearvideo.com/'+li.xpath('./div/a/@href')[0]
        name = li.xpath('./div/a/div[2]/text()')[0]+'.mp4'
        # print(detail_url,name)
        #对详情页的url发请求
        detail_page_text= requests.get(url=detail_url,headers=headers).text
        treee = etree.HTML(detail_page_text)
        data_id = treee.xpath('//*[@id="poster"]/@data-cid')[0]
        mrd = random.random()
        # print(mrd)
        video_url = "https://www.pearvideo.com/videoStatus.jsp?contId="+data_id
        print(video_url)
        data = {
            'contId':data_id,
            'mrd':mrd,
            'name':name,
            'url':video_url
        }
        urls.append(data)
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36',
            'Referer':'https://www.pearvideo.com/video_'+data_id
        }
        # print(data)
    # print(urls)
    pool = Pool(4)
    pool.map(get_video_data,urls)
    pool.close()
    pool.join()
