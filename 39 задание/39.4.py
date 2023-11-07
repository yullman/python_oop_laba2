class User:
    _name = None
    _age = None

    def setName(self, name):
        self._name = name

    def getName(self):
        return self._name

    def setAge(self, age):
        self._age = age

    def getAge(self):
        return self._age

class Employee(User):
    salary = None

    def setSalary(self, salary):
        self._salary = salary

class Programmer(Employee):
    _numbers = 22222

    def printik(self):
        print(self._numbers)

class Designer(Employee):
    _test = 11111
    def printikAll(self):
        print(self._test, self.salary)