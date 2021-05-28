# class 类名  类名要符合  大驼峰命名法
class Cat:

    def eat(self):
        # 哪一个对象调用的方法，self就是哪一个对象的引用
        print('{0}爱吃鱼'.format( self.name))

    def drink(self):
        print('小猫要喝水')



# 创键猫对象
tom =Cat()
tom.name = "Tom"
tom.eat()
tom.drink()

# 在创建一个猫对象

lazy_cat= Cat()
lazy_cat.name = 'lazy_cat'
lazy_cat2 = lazy_cat

lazy_cat.eat()

lazy_cat.drink()

print(tom)
print(tom.name)
print(lazy_cat)
print(lazy_cat2)



