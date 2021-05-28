class A:

    def test(self):
        print("A --- test method")

    def demo(self):
        print("A --- demo method")

class B:

    def demo(self):
        print("B --- demo method")

    def test(self):
        print("B --- test method")


class C(B, A):
    """多继承可以让子类对象同时具有多个父类的属性和方法"""
    pass


# 创建子类对象
c = C()

c.test()
c.demo()

# 确定C类对象调用对象的顺序
print(C.__mro__)