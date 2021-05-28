"""python中的类还支持多继承"""
class Scale:
    def check(self):
        if self.count_person > 500:
            print("%s is big company"%self.name)
        else:
            print("%s is small company"%self.name)

class Detail:
    def show(self,scale):
        print("%s,there seems %s staff in the company."%(scale,self.count_person))

class Company(Scale,Detail):
    def __init__(self,name,count):
        self.name = name
        self.count_person = count
    # 子类会继承父类的方法

if __name__ == '__main__':
    my_company = Company("ABC",800)
    my_company.check()
    my_company.show(my_company)