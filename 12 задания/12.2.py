class Employee():
    age = None
    name = None
    slary = None
    def __init__(self,name,slary):
        self.name = name
        self.slary = slary
    def imya(self):
        print(self.name)
one = Employee('иванчик',100000)
one.imya()