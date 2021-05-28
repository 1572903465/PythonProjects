import threading
import time

event = threading.Event()

def cal(name):
    print('%s start!\n'%threading.current_thread().getName())
    print('%s is waiting for event.\n'%name)
    event.wait()
    print('%s get informed.\n'%threading.current_thread().getName())
    print('%s start work!'%name)

if __name__ == '__main__':
    threading.Thread(target=cal,args=('Alice',)).start()
    threading.Thread(target=cal,args=('Bob',)).start()
    time.sleep(3)
    event.set()