import threading

class Rlock_Data():
    rlock = threading.RLock()#递归锁
    def __init__(self):
        self.data = 0
    
    def execute(self,n):
        with Rlock_Data.rlock:#自动开关
            self.data += n
    
    def add(self):#加 1 操作
        with Rlock_Data.rlock:#自动开关
            self.execute(1)
    
    def down(self):#减 1 操作
        with Rlock_Data.rlock:#自动开关
            self.execute(-1)

def add_data(rlock):
  
    for _ in range(1000000):#连续加 一百万次
        rlock.add()

def down_data(rlock):
   
    for _ in range(1000000):#连续减 一百万次
        rlock.down()
    
if __name__ == "__main__":
    print('程序开始')
    t = Rlock_Data()
    t1 = threading.Thread(target = add_data,args=(t,))#target参数填函数名 不要用括号
    t2 = threading.Thread(target = down_data,args=(t,))#args参数把Rlock_Data实例传进去
    t1.start()#开始执行
    t2.start()

    t1.join()#堵塞线程
    t2.join()
    print(t.data)
    print('程序结束')