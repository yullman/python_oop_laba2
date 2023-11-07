class Employee():
    __age = None
    __name = None
    __slary = None
    def setName(self,name):
        self.__name=name
    def setAge(self,age):
        if 0 < age < 120:
            self.__age=age
        else:
            print('неверный возраст')
    def setSlary(self,slary):
        self.__slary=slary
    def getName(self):
        print(self.__name)
    def getAge(self):
        print(self.__age)
    def getSlary(self):
        print(self.__slary)

one = Employee()
one.setSlary(10000)
one.setAge(111)
one.setName('ванька')
one.getAge()
one.getName()
one.getSlary()