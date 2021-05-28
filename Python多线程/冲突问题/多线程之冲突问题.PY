import threading

data = 0

def add_data():
    global data
    for _ in range(1000000):#连续加 一百万次
        data += 1

def down_data():
    global data
    for _ in range(1000000):#连续减 一百万次
        data -= 1
    
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

#两个线程 操作 同一个变量
#最后得到的数字是 混乱的  不确定的
#这是为什么呢？

#线程操作有两步：
# 1.计算   2.赋值

#一号线程 负责一直加  123456789
#二号线程 负责一直减  疯狂减 1
#当一号线程计算了  还没来得及赋值  二号线程就开始减1
#所以导致出现负数情况  