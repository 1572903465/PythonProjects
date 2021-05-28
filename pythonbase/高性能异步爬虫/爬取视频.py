import  requests,os,re
from multiprocessing import Pool
import threading
from concurrent.futures import ThreadPoolExecutor
from lxml import  etree
def getVedioData(dic):
    url = dic['url']
    name = dic['name']
    header = dic['header']
    vedio_data = requests.get(url=url,headers = header).content
    print("正在下载视频：",name,",下载地址为：",url)
    print('当前子线程：', threading.current_thread().getName(), '当前父进程', os.getppid(), '当前子进程', os.getpid())
    with open('./down/'+name,'wb') as fp:
        fp.write(vedio_data)
if __name__ == "__main__":
    url = 'https://www.pearvideo.com/category_5'
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Wisn64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
    }
    param = {

    }
    if not os.path.exists('./down'):
        os.mkdir('./down')
    page_text = requests.get(url=url, params = param ,headers = header ).text
    tree = etree.HTML(page_text)
    list_a = tree.xpath('//li[@class="categoryem"]//a[contains(@class,"vervideo-lilink")]')
    temp_ajax_taget = "https://www.pearvideo.com/videoStatus.jsp?contId="
    #遍历每个视频详情页a标签，拿到名称和number就ok
    ajax_dic = []
    for i in list_a:
        #拿到名称
        tempName = i.xpath('./div[@class="vervideo-title"]/text()')[0] + '.mp4'
        #从video_1710111中拿到数字
        temp_ajax_Url_number =re.findall( 'video_(.*)', i.xpath("./@href")[0])[0]
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Wisn64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
            'Referer': "https://www.pearvideo.com/video_" + temp_ajax_Url_number
        }
        #拼接ajax请求
        temp_ajax_Url = temp_ajax_taget+temp_ajax_Url_number
        print(temp_ajax_Url)
        #json转换成为字典
        # temp_ajax_text =requests.get(url=temp_ajax_Url,headers = header).json()
        #json转换成字符串
        temp_ajax_text = requests.get(url=temp_ajax_Url, headers=header).text
        #拿到视频下载链接的半成品
        # https://video.pearvideo.com/mp4/third/20201203/1607225679010-15025517-145355-hd.mp4
        srcUrl = re.findall('"srcUrl":"(.*?)"',temp_ajax_text)[0]
        #修改时间戳，数字前面得加con，梨视频的手脚
        cont = 'cont-' + temp_ajax_Url_number
        #转换后
        #https://video.pearvideo.com/mp4/third/20201203/cont-1710009-15025517-145355-hd.mp4
        new_srcUrl = srcUrl.replace(srcUrl.split("-")[0].split("/")[-1], cont)
        print(new_srcUrl)
        #把ajax下载链接和视频名称存储起来
        dic = {
            'name':tempName,
            'url':new_srcUrl,
            'header':header
        }
        ajax_dic.append(dic)
    #利用线程池创建多个线程调用请求下载操作
    pool = ThreadPoolExecutor(5,thread_name_prefix="test_")
    # pool.map(getVedioData,ajax_dic)
    for i in ajax_dic:
        pool.submit(getVedioData,i)
    pool.shutdown()
    #线程礼让，让主线程别急着结束，等待pool子线程结束才结束
    #网友：pool.join() 代表 主进程阻塞后，让子进程继续运行完成，子进程运行完后，再把主进程全部关掉。
    #但这又不是守护进程，默认不应该是子线程没结束，主线程不能结束嘛
    #join方法的作用是阻塞，等待子线程结束，join方法有一个参数是timeout，即如果主线程等待timeout，子线程还没有结束，则主线程强制结束子线程。
    # pool.join()
