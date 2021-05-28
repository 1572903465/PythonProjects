import threading
import time
class Account:
    def __init__(self,account_no,balance):
        self.account_no = account_no
        self._balance = balance
        self.lock = threading.RLock()

    def getBalance(self):
        return self._balance
    def draw(self,draw_amount):
        self.lock.acquire()
        try:
            if self._balance >= draw_amount:
                print(threading.current_thread().name\
                      +"success!Waiting for cash"+str(draw_amount))
                time.sleep(0.001)
                self._balance-=draw_amount
                print("The Balance is :",str(self._balance))
            else:
                print(threading.current_thread().name+"failed!The Balance is insufficient!")
        finally:
            self.lock.release()

if __name__ == '__main__':
    def draw(acount,draw_amount):
        acount.draw(draw_amount)
    acct = Account("1234567",1000)
    threading.Thread(name="Alice",target=draw,args=(acct,800)).start()
    threading.Thread(name="Bob",target=draw,args=(acct,800)).start()