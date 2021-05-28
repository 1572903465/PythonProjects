# from _01_测试模块1 import Dog,say_hello
from _02_测试模块2 import say_hello as Module2_say_hello
from _01_测试模块1 import Dog,say_hello

say_hello()
Module2_say_hello()
dog = Dog()
print(dog)
print(Dog)