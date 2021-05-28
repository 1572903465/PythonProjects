class animals:
    def breath(self):
        print('呼吸')

class mammals(animals):
    def move(self):
        print('奔跑')

class dog(mammals):
    def eat(self):
        print('吃')

if __name__ == '__main__':

    Bob = dog()
    Bob.move()
    Bob.eat()
