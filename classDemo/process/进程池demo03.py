from multiprocessing import Pool
from time import sleep, ctime


def event(message):
    sleep(1)
    print(ctime(), ':', message)
    return '&' + str(message) + '&'

if __name__ == '__main__':

    pool = Pool(4)

    print(ctime())
    # 阻塞,返回值为列表
    l = pool.map(event, range(10))
    # 非阻塞,返回值为对象，使用get()方法获取列表,get()会阻塞
    # l = pool.map_async(event, range(10))

    print(l)
    #print(l.get())

    pool.close()
    pool.join()

    print(ctime())