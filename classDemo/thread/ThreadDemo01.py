from threading import *
import time

def func(arg):
    time.sleep(1)
    print('thread'+str(arg)+"running...")

if __name__ == '__main__':
    for i in range(10):
        t = Thread(target=func,args=(i,))
        t.start()