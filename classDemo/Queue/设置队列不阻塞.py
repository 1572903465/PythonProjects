# 先进先出队列
import queue

# 最多接收10个数据
q = queue.Queue(2)

# put 向队列中添加数据
q.put(15)
q.put(59)

# 设置队列不阻塞(当队列满的时候再插入数据,直接报错)
q.put('PolarSnow', block=False)

# 获取当前队列长度
print(q.qsize())

# 取出最前面的一个数据
print(q.get())
#默认程序会阻塞，等待新的值插入到队列当中，使用了block=False参数后，强制设置为不阻塞，一旦超出队列长度，立即抛出异常