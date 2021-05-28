import time
import threading

def run(n,se):
    se.acquire()
    print("run the thread-%s"%n)
    time.sleep(0.5)
    se.release()

if __name__ == '__main__':
    semaphore = threading.BoundedSemaphore(3)
    for i in range(9):
        t = threading.Thread(target=run,args=(i,semaphore))
        t.start()
