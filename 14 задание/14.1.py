class Employee:
  def __init__(self,name, salary):
    self.name = name
    self.salary = salary
    def getSalary(self):
        return self.addSign(self.salary)
    def __addSign(self,num):
       return num + '$'