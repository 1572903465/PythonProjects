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

# 创建了一个对象  -狗对象

wangcai  = Dog()

wangcai.eat()
wangcai.drink()
wangcai.sleep()
wangcai.run()
wangcai.bark()
