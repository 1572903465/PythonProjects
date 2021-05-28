class Women:
    #  在定义属性或者方法时，在属性名或者方法名前增加两个下划线，定义的就是 私有 属性或方法
    def __init__(self, name):
        self.name = name
        self.__age = 18

    def __secret(self):
        # 在对象的方法内部是可以访问对象的私有属性的
        print("%s 的年龄是 %d" % (self.name, self.__age))


xiaofang = Women("小芳")
# 1. 私有属性在外界不能够被直接访问
print(xiaofang._Women__age)

# 2. 私有方法同样不允许在外界直接访问
xiaofang._Women__secret()

