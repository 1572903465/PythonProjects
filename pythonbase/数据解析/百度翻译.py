import requests
from lxml import etree

if __name__ == '__main__':
    url='https://dict.youdao.com/w/eng/{}/#keyfrom=dict2.index'
    headers = {
        'Origin': 'https: // fanyi.baidu.com',
        'Cookie':'BAIDUID=EE11ACEAEAB37C55DBDD9AAB8FBCB845:FG=1; ab_jid=6107055f23d98c4514fe7c24c78271b784f1; ab_jid_BFESS=6107055f23d98c4514fe7c24c78271b784f1; BIDUPSID=EE11ACEAEAB37C55DBDD9AAB8FBCB845; PSTM=1602744047; BAIDUID_BFESS=C0B51A28F7EEC7ECE0BC52A8701A4315:FG=1; __yjs_duid=1_ce00968aade9720368f9f49ee765d2f61616944618872; ab_sr=1.0.0_ZmQxOTBjZDgyZTBmMDE0NzQyYzA4Mzk4NTFhMzU5NjNlNGM4NDdkMmE5ZDY4OThjZTJlMTQ5NzU0ODE3OTBjNDk5YjkxNDUzNDBjMTVhZmQzMDFlNGVlZjdkZjUwZjY1; __yjs_st=2_MTQwODI4YTM4YWJiNDBmNmMxNDk0MzRkMGIzNTdkMzczMTU5MDNlZDNmMDZmNGI4ODZkN2YzZjg3OTUwYWM2NmVjMjJjNDgzZTM2ODIwMTYyMTRmNDU3MTY2ZmRiM2E5YmMxOGY2YWQ5YWRmYzdlY2ExODU5MWJiMDA2YmNjNDIyYjYzMWM0MThkMzQ3MTk1YjhhZmNiODg3OWY0NDViYmRkNTQyM2I2OWVlNjNhNmJiYTNhMDZmMzE4ZmNiNjVjYWZiYTcwOTAwM2MzOTNmYWI1ZWY0ODhkZWI3MWQxNDgzY2NmMWQ2YmJmNTUwM2ZjMzE5MDMxYzc5NzJlODZmMF83X2YyMDVkNDE5',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0'
    }
    word='dog'
    url = url.format(word)
    print(url)
    page_text = requests.get(url=url,headers=headers).text
    # print(page_text)
    tree=etree.HTML(page_text)
    div = tree.xpath('//*[@id="phrsListTab"]/h2/div/span/span/text()')
    li_list= tree.xpath('//*[@id="phrsListTab"]/div[2]/ul/li/text()|//*[@id="phrsListTab"]/div/ul/li/text()')

    print(div)
    print(li_list)

