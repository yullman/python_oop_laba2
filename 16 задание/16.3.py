class Employee():
    __age = None
    __name = None
    __slary = None
    def __init__(self,name,slary,age):
        self.__name = name
        self.__age = age
        self.__slary = slary
    def getName(self):
        print(self.__name)
    def getAge(self):
        print(self.__age)
    def getSlary(self):
        print(self.__slary)

one = Employee('санька',120000,30)
one.getAge()
one.getName()
one.getSlary()