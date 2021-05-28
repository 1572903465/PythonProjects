class Car:

    def run(self):
        print("running")

    def stop(self):
        print("stopping")

class BWM(Car):

    def run(self):
        print("BWM -->> runing")

    def stop(self):
        print("BWM -->> stopping")

class Fute(Car):

    def run(self):
        print("Fute -->> running")

    def stop(self):
        print("Fute -->> stopping")

class Phoenix(Car):

    def run(self):
        print("Phoenix -->> running")

    def stop(self):
        print("Phoenix -->> stopping")

class CarFactory:
    """ 工厂集中管理"""
    def new_car(self, name):
        if name == "BMW" :
            bwm = BWM()
            return bwm

        if name == "Phoenix":
            phoenix = Phoenix()
            return phoenix

        if name == "Fute":
            fute = Fute()
            return fute

class CarStore:
    """4S店"""
    def __init__(self, factory):
        self.factory = factory

    def order(self,name):
        """订单"""
        new_car = self.factory.new_car(name)
        return new_car


factory = CarFactory()

car_store = CarStore(factory)

fh = car_store.order("Phoenix")
fh.run()
fh.stop()



