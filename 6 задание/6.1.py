class Employee():
    age = None
    name = None
    slary = None
    def metod(self, name,slary):
        slary = str(slary)
        return name + " " + slary
user = Employee()
print(user.metod('саня', 15000))
        
