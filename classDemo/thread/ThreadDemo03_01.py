import threading
import time

number = 0

def plus():
    global number;
    for i in range(1000000):
        number += 1
    print("When %s completes ,number = %s\n"\
          %(threading.current_thread().getName(),number))

if __name__ == '__main__':
    for i in range(2):
        t = threading.Thread(target=plus)
        t.start()
        t.join()     #add  join()
time.sleep(2)
print("when main thread completes,number = ",number)