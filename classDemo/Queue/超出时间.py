# 先进先出队列
import queue

# 最多接收10个数据
q = queue.Queue(2)

# put 向队列中添加数据
q.put(15)
q.put(59)
print(q.qsize())

# 超时时间为2秒
q.put('PolarSnow', timeout=2)

# 获取当前队列长度
print(q.qsize())

# 取出最前面的一个数据
print(q.get())

#现在队列的最大长度设置为2，当第三个数据向里面插入时，最多等待两秒，两秒后还没有进入到队列中就报错