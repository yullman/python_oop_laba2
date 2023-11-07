class Employee:
    __name =    None
    __salary = None

    def __init__(self, name, age, salary):
        self.__name = name
        self.__salary = salary

    def getName(self):
        return self.__name

    def getSalary(self):
        return str(self.__salary) + "$"

    def setName(self, name):
        self.__name = name

    def setSalary(self, salary):
        self.__salary = salary