class User:
    name = None
    position = None
    department = None

    def __init__(self, name, position, department):
        self.name = name
        self.position = position
        self.department = department


class Employee:
    company = None
    status = None

    def __init__(self, company, status):
        self.department = company
        self.position = status

rab = Employee('corp', 'manager')
egor = User('egor', rab.position, rab.department)
print(egor.name, egor.department, egor.position)