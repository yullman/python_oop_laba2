class Employee:
    __name = None
    __surname = None
    __salary=  None

    def __init__(self, name, surname, salary):
        self.__name = name
        self.__surname = surname
        self.__salary = salary

    def getName(self):
        return self.__name

    def getSurname(self):
        return self.__surname

    def getSalary(self):
        return str(self.__salary) + "$"

    def setName(self, name):
        self.__name = name

    def setSurname(self, surname):
        self.__surname = surname

    def setSalary(self, salary):
        self.__salary = salary
        
employee = Employee("vanya", 'vanin', 10)
print(employee.getName())
print(employee.getSurname())
print(employee.getSalary())
employee.setName("ffwe")
employee.setSurname('ewefw')
employee.setSalary(124351)
print(employee.getName())
print(employee.getSurname())
print(employee.getSalary())