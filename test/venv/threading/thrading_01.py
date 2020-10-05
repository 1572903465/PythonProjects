import threading
import time

number = 0
lock = threading.Lock()

def plus():
    global  number
    lock.acquire()
    for i in range(1000000):
        number+=1
    print("When its completes,number = ",(threading.current_thread().getName(),number))
    lock.release()

if __name__ == '__main__':
    for i in range(2):
        t = threading.Thread(target=plus)
        t.start()
    time.sleep(2)
    print("When main thread completes,number = ",number)
