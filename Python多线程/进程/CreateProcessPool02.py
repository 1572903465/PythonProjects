import multiprocessing#导入进程包
import os,time#这两个包的作用皆为更好的体现出我们的进程
def copy(index):
    print("当前进程编号",os.getpid())
    print(index)
    time.sleep(1)#打一个时间差，更容易看出其效果
if __name__ == '__main__':
    pool = multiprocessing.Pool(3)#导入进程池，括号内为最大进程数
    for i in range(10):
        pool.apply_async(copy,(i,))
    pool.close()
    pool.join()