class dog(object):
    """狗类的创键例子"""

    def __init__(self,name,kind,month_age):  #类的构造方法
         self.name = name
         self.kind = kind
         self.month_age = month_age

    def __str__(self):
        return '<狗名：%s（%s,%d个月)>' %(self.name,self.kind,self.month_age)

    def bark(self):  #类方法必须包含参数self
        print('汪汪')


if __name__ == '__main__':
    Bob = dog('Bob','金毛',9)
    print(Bob)
    Bob.bark()  #执行实例的方法不加参数self