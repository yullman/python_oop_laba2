class Employee:
    __age = None

    def __init__(self,age):
        self.__age = age

    def getAge(self):
        return self.__age
    
    def setAge(self, age):
        self.__age=age