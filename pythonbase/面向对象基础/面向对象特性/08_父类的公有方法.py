class A:

    def __init__(self):
        self.num1 = 100
        self.__num2 = 200

    def __test(self):
        print("私有方法%d %d" % (self.num1, self.__num2))

    def test(self):
        print("公有方法%d %d"%(self.num1,self.__num2))
        self.__test()


class B(A):

    def demo(self):
        # 1. 在子类的对象方法中，不能访问父类的私有属性
        # print("访问父类的私有属性 %d"%self.__num2)
        # 2. 在子类的对象方法中，不能访问父类的私有属性
        # self.__test()
        # 3.访问父类的公有属性
        print("子类方法%d"%self.num1)
        # 4。调用父类的公有方法
        self.test()
        pass


# 创建一个子类对象
b = B()
print(b.num1)
b.demo()
# 在外界访问父类发公有属性/调用公有方法
b.test()

# 子类在外界不能直接访问父类的私有属性和调用私有方法
# print(b.num2)
# b.__test()