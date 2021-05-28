# 先进先出队列
import queue

# 最多接收10个数据
q = queue.Queue(10)

# put 向队列中添加数据
q.put(15)
q.put(59)

# 获取当前队列长度
print(q.qsize())

# 取出最前面的一个数据
print(q.get())