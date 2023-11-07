class Employee():
    age = None
    name = None
    slary = None
one=Employee()
two = Employee()
one.name = 'артем'
one.slary = 100000
two.name = 'вася'
two.slary = 120000
print(one.slary+two.slary)