class Employee():
    __age = None
    __name = None
    __slary = None
    def __init__(self,name,slary,age):
        self.__name = name
        self.__age = age
        self.__slary = slary
    def vivod(self):
        print(self.__name,self.__age,self.__slary)
one = Employee('санька',120000,30)
one.vivod()