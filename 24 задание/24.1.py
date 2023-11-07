class Employee:
    name = None
    company = None
    status = None
    salary = None

    def __init__(self, name, company, status, salary):
        self.name = name
        self.company = company
        self.status = status
        self.salary = salary


rabi = [
    Employee('egor', 'corp', 'Manager', '3500234232423423423'),
    Employee('grerger', 'wgfwef', 'wfger', '423423'),
    Employee('jhon', 'firma', 'sotrudnik', '50000')
]