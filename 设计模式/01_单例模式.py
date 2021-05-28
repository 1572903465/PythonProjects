class Sun:
    # define class
    __instance = None
    def __new__(cls, *args, **kwargs):
        # 如果__instance还没有值，就给__instance变量赋值
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
            return cls.__instance
        else:
            return  cls.__instance

sun = Sun()
sun1 = Sun()
sun2 = Sun()
print(sun is sun1)
print(id(sun))
print(id(sun1))
print(id(sun2))


class Car:
    def __new__(cls, *args, **kwargs):
        # 如果Car没有instance的这个属性
        if not hasattr(Car,"instance"):
            Car.instance = object.__new__(cls)
        return Car.instance

    def __init__(self,name,cid):
        self.name = name
        self.cid = cid

bmw = Car("宝马X5","666666")
bnze = Car("奔驰","55455")

print(bmw is bnze)
print(bmw)
print(bnze)
