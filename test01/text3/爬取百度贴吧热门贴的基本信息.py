import requests
import re
if __name__ == '__main__':
    url = 'https://tieba.baidu.com/p/6156634738'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'
    }
    params = {
        'pn':'1'
    }
    page_text = requests.get(url=url,headers=headers,params=params).text
    # print(page_text)
    ex1 = 'target="_blank">(.*?)<img src'
    name = re.findall(ex1,page_text)[0]
    print('发帖人：',name)
    time = re.findall('<span class="tail-info">1楼</span><span class="tail-info">(.*?)</span>',page_text)[0]
    print('发帖时间：',time)
    content = re.findall('<div id="post_content_126003994602" class="d_post_content j_d_post_content " style="display:;">(.*?)<br>',page_text)[0]
    print('发帖内容：',content)
    floor = re.findall('<span class="red" style="margin-right:3px">(.*?)</span>',page_text)[0]
    print('楼层数：',floor)
