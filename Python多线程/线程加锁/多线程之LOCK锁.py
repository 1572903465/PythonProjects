import threading

lock = threading.Lock()#普通锁 重量级锁 
data = 0

def add_data():
    global data
    for _ in range(1000000):#连续加 一百万次  
        lock.acquire()#锁上
        data += 1           
        lock.release()#解锁

def down_data():
    global data
    for _ in range(1000000):#连续减 一百万次
        lock.acquire()#锁上
        data -= 1
        lock.release()#解锁
    
if __name__ == "__main__":
    print('程序开始')
    t = threading.Thread(target = add_data)#target参数填函数名   不要加括号
    t2 = threading.Thread(target = down_data) 
    t.start()#开始执行
    t2.start()

    t.join()#堵塞线程
    t2.join()
    print(data)
    print('程序结束')