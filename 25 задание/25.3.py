class EmployeeCollection:
    __emps = None

    def __init__(self):
        self.__emps = []

    def add(self, emp):
        self.__emps.append(emp)

    def show(self):
        for emp in self.__emps:
            print(emp.getName())
