# class 类名  类名要符合  大驼峰命名法
class Cat:

    def eat(self):
        print('小猫爱吃鱼')

    def drink(self):
        print('小猫要喝水')



# 创键猫对象
tom =Cat()
tom.eat()
tom.drink()
#dir内置函数可以查看对象的所有方法
print(dir(tom))

print(tom)

addr = id(tom)

# %d 输出10进制  %X 输出16进制
print("%d"%addr,"%X"%addr)

