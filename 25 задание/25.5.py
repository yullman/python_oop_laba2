class EmployeeCollection:
    __emps = None

    def __init__(self):
        self.__emps = []

    def add(self, emp):
        self.__emps.append(emp)

    def show(self):
        for emp in self.__emps:
            print(emp.getName())

    def sum_sal(self):
        summ_sal = 0
        for emp in self.__emps:
            summ_sal += int(emp.salary)

    def mid_sal(self, summ_sal):
        total = summ_sal / len(self.__emps)