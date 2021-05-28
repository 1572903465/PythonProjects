from multiprocessing import Pool
import os,time,random

def  worker(msg):
    t_start = time.time()
    print("%s开始执行，进程号为%d"%(msg,os.getpid()))
    time.sleep(random.random()*2)
    t_stop = time.time()
    print(msg,"执行完毕，耗时%0.2f"%(t_stop-t_start))
if __name__ == '__main__':
    po = Pool(3)   #定义进程池
    for i in range(0,10):
        po.apply_async(worker,(i,))
   #     po.apply(worker,(i,).)

    print("----start-----")
    po.close()  #关闭进程池，关闭后po不再接收新的请求
    po.join()   #占用全部资源，等待po中所有的子进程执行完成，必须放在close后
    print("---end---")
