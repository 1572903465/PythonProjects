import time
import threading

#GIL是解释器用于同步线程的一种机制
#它使得任何时刻仅有一个线程在执行 (就算你是多核处理器也一样)
#使用GIL的解释器只允许同一时间执行一个线程
#常见的使用GIL的解释器有 CPython 与 Ruby MRI
#如果你用JPython没有GIL锁

#CPU 多线程
def start():#单纯计算  消耗CPU资源  没有实际意义
    data = 0
    for _ in range(10000000):#连续加
        data += 1

    return

if __name__ == "__main__":
    
    time_data = time.time()
    ts = {}

    for i in range(10):
        t = threading.Thread(target = start)#target参数填函数名 不要用括号
        t.start()
        ts[i] = t  #全新的线程

    for i in range(10):
        ts[i].join()

    print(time.time() - time_data)