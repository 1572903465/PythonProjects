import threading
import time

number = 0
lock = threading.Lock()

def plus(lk):
    global number;
    lk.acquire()    # acquire lock
    for i in range(1000000):
        number += 1
    print("When %s completes ,number = %s\n"\
          %(threading.current_thread().getName(),number))
    lk.release()    #解锁

if __name__ == '__main__':
    for i in range(2):
        t = threading.Thread(target=plus,args=(lock,))
        t.start()

time.sleep(2)
print("when main thread completes,number = ",number)