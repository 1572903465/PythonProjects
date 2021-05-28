import multiprocessing
#from multiprocessing import Process,Manager,Pool

def download_from_web(q):
    #模拟从网上下载数据
    data = [11,22,33,44]

    #向队列中写入数据
    for temp in data:
        q.put(temp)

    print("----下载器已经下载完了并且存入到队列中----")

def analysis_data(q):
    #数据处理
    waitting_analysis_data=list()
    #从队列中获取数据
    while True:
        data = q.get()
        waitting_analysis_data.append(data)
        if q.empty():
            break
    print(waitting_analysis_data)

def main():
    q = multiprocessing.Manager().Queue()
    pool = multiprocessing.Pool(3)
    pool.apply_async(download_from_web,(q,))
    pool.apply_async(analysis_data,(q,))
    pool.close()
    pool.join()

if __name__ == '__main__':
    main()