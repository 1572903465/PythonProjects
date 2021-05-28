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

# 在创建一个猫对象

lazy_cat= Cat()

lazy_cat2 = lazy_cat
lazy_cat.eat()
lazy_cat.drink()
print(tom)
print(lazy_cat)
print(lazy_cat2)



