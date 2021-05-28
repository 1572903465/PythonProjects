class Animal:
    def eat(self):
        print("吃")

    def drink(self):
        print("喝")

    def run(self):
        print("跑")

    def sleep(self):
        print("睡")

#  子类拥有父类的属性和方法
class Dog(Animal):

    # def eat(self):
    #     print("吃")
    #
    # def drink(self):
    #     print("喝")
    #
    # def run(self):
    #     print("跑")
    #
    # def sleep(self):
    #     print("睡")

    def bark(self):
        print("汪汪叫")

class Cat(Animal):

    def catch(self):
        print("抓老鼠")

class XiaoTianQuan(Dog):

    def fly(self):
        print("我会飞")


# 创建了一个对象  -狗对象

xtq = XiaoTianQuan()
xtq.fly()
xtq.bark()
xtq.eat()
# xtq.catrh()