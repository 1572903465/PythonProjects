"""使用"apply_async()"需要自己创建列表，维护返回值'"""
from multiprocessing import Pool
from time import sleep, ctime


def event(message):
    sleep(2)
    print(ctime(), ':', message)
    return '&' + str(message) + '&'

if __name__ == '__main__':
    print(ctime())
    pool = Pool(4)
    r_list = []

    for i in range(10):
        # apply效率非常低，进程池中同一时刻，只有一个进程在运行。
        # 程序在此处阻塞

        # element = pool.apply(event,(i,))
        # apply_async可以提升效率：进程池中的进程并行执行，一起返回，直到所有进程都执行完毕;
        # 程序在此处并不会阻塞
        element = pool.apply_async(event, (i,))
        print(element)
        r_list.append(element)

    for e in r_list:
        # print(e)
        # apply_async返回事件对象,可通过get()方法获取事件函数返回值
        print(e.get())

    print(ctime())

    pool.close()
    pool.join()
