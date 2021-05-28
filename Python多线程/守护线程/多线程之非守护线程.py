import threading
import time

def start():
    time.sleep(2)
    print(threading.current_thread().name)#打印线程名字
    print(threading.current_thread().isAlive())#打印当前线程还活着
    print(threading.current_thread().ident)#打印当前线程的ID

if __name__ == "__main__":#主线程 
    print('程序开始')
    #以下是我们创建的线程    主线程 会跳过 创建线程 
    t = threading.Thread(target = start,name = '我的第一个线程')#target参数填函数名 不要用括号
    t.start()#开始执行
    # t.join()#堵塞线程
    print('程序结束')