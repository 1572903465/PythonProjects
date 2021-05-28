import threading
import time


class TestThread(threading.Thread):  #1. 继承语法：class派生类名（基类名）

    def __iadd__(self, name=None):              # 2.构造方法： __init__(sele,name=None)
        threading.Thread.__init__(self,name=name)
    def run(self):                                  #3.需要的任务函数通过重写run方法完成
        for i in range(5):
            print(threading.current_thread().name+'test',i)
            time.sleep(1)

if __name__ == '__main__':
    t = TestThread(name='TestThread')
    t.start()