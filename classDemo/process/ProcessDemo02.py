from multiprocessing import Process
import os

def action(name,*add):
    print(name)
    for arc in add:
        print("%s --current processid is %d"%(arc,os.getpid()))

class My_Process(Process):

    def __init__(self,name,*add):
        super().__init__()
        self.name = name
        self.add = add

    def run(self):
        print(self.name)
        for arc in self.add:
            print("%s--curent process id is %d"%(arc,os.getpid()))
if __name__ == '__main__':
    print("Current process id:",os.getpid())
    my_tule = ("Alice","Bob","Calvin")
    my_process = My_Process("my_process",*my_tule)
    my_process.start()
    action("main process",*my_tule)