import requests,os
from lxml import etree
from multiprocessing.dummy import Pool

def get_img(img):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'
    }
    img_data = requests.get(url=img['url'], headers=headers).content
    with open(img['path'],'wb') as fp:
        fp.write(img_data)
        print(img['name'],'下载成功！！！')

if __name__ == '__main__':
    url = 'http://pic.netbian.com/4kmeinv/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'
    }
    response = requests.get(url=url,headers=headers)
    # response.encoding = 'utf-8'
    page_text = response.text
    # print(page_text)
    tree = etree.HTML(page_text)
    li_list = tree.xpath('//div[@class="slist"]/ul/li')
    # print(li_list)
    #创建一个文件夹
    if not os.path.exists('./picLibs'):
        os.mkdir('./picLibs')
    url_data = []
    for li in li_list:
        img_src = 'http://pic.netbian.com'+li.xpath('./a/img/@src')[0]
        img_name = li.xpath('./a/img/@alt')[0]+'.jpg'
        img_name = img_name.encode('iso-8859-1').decode('gbk')
        # print(img_name)
        # img_data = requests.get(url=img_src,headers=headers).content
        img_path = 'picLibs/'+img_name
        data = {
            'name' : img_name,
            'url' : img_src,
            'path' :img_path
        }
        url_data.append(data)
    pool = Pool(5)
    pool.map(get_img,url_data)
    pool.close()
    pool.join()


