import _01_测试模块1 as DogModule
import _02_测试模块2 as CatModule
"""as 给模块取别名，命名规则大驼峰命名法"""

DogModule.say_hello()
CatModule.say_hello()

dog = DogModule.Dog()
print(dog)

cat = CatModule.Cat()
print(cat)