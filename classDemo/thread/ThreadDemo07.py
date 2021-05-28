import threading

cv = threading.Condition()
alist = []

def product():
    global alist
    cv.acquire()
    print('producer acquire lock')
    for i in range(10):
        alist.append(i)
    cv.release()
    print('producer release lock')

def consumer():
    cv.acquire()
    print('consumer acquire lock')
    while not alist:
        print('consumer wait and release lock')
        cv.wait()
    print('wait threading acquire lock')
    print(alist)

if __name__ == '__main__':
    tproducer = threading.Thread(target=product)
    tconsumer = threading.Thread(target=consumer)
    tproducer.start()
    tconsumer.start()