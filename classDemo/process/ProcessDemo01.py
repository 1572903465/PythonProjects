from multiprocessing import Process
import os

def action(name,*add):
    print(name)
    for arc in add:
        print("%s -- current process id is %d"%(arc,os.getpid()))

if __name__ == '__main__':
    print("Current process id:",os.getpid())
    my_tuple = ("Alice","Bob","Calvin")
    #child process
    my_process = Process(target=action,args=("my_process",*my_tuple))

    my_process.start()
    # Main process
    action("mian process",*my_tuple)