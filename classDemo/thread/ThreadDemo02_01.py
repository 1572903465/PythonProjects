import threading

def action(*add):
    for arc in add:
        print(threading.current_thread().getName()+' '+arc)

my_tuple=("Alice","Bob","Calvin")

if __name__ == '__main__':

    thread = threading.Thread(target=action,args=my_tuple)
    thread.start()
    for i in range(5):
        print(threading.current_thread().getName())