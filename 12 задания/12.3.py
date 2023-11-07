class Employee():
    age = None
    name = None
    slary = None
    def __init__(self,name,slary):
        self.name = name
        self.slary = slary
    def zp(self):
        print(self.slary)
one = Employee('иванчик',100000)
one.zp()