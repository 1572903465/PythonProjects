import time

#CPU 裸奔
def start():#单纯计算  消耗CPU资源  没有实际意义
    data = 0

    for _ in range(10000000):
        data += 1

    return

if __name__ == "__main__":
    
    time_data = time.time()#程序启动时间

    for _ in range(10):#执行10次   这个 _ 代表 我们不打算使用这个变量
        start()

    print(time.time() - time_data)#当前时间 减去 启动时间 = 程序过程耗时