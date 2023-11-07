class Employee:
    __name = None

    def __init__(self, name, age, salary):
        self.__salary = salary

    def getSalary(self):
        return str(self.__salary) + "$"

    def setSalary(self, salary):
        self.__salary = salary