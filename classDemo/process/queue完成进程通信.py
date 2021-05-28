from multiprocessing import Queue
def main():
    q = Queue(3) #初始化一个Queue对象，最多可接受三条消息
    q.put('messmag1')
    q.put('message2')
    print(q.full())
    q.put('message3')
    print(q.full())
    try:
        q.put('message4')
    except:
        print('消息队列已满，现有消息数量：%s'%q.qsize())
    try:
        q.put_nowait('message4')
    except:
        print('消息队列已满，现有消息数量：%s' % q.qsize())
    if not q.full():
        q.put_nowait('message4')

    if not q.empty():
        for i in range(q.qsize()):
            print(q.get_nowait)
if __name__ == '__main__':
    main()