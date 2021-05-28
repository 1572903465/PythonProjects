class Company:
    def __init__(self, companyname, leader):
        self.companyname = companyname
        self.leader = leader

    def show(self):
        print(self.companyname)
        print(self.leader)

if __name__ == '__main__':
    obj1 = Company('A','Kevin')
    obj2 = Company('B','Jone')

    #通过对象直接调用封装的数据
    print(obj1.companyname)
    print(obj1.leader)

    #通过self来间接调用，self即对象本身
    obj1.show()
    obj2.show()