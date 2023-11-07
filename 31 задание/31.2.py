class Employee:
    __age = None

    def __init__(self,age):
        self.__age = age

    def getAge(self):
        return self.__age
    
    def setAge(self, age):
        if 18 <= age <= 65:
            self.__age=age
        else:
            print("неверный возраст")