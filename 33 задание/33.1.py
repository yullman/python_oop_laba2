class User:
	def __init__(self, name, surname) -> None:
		self.name = name
		self.surname = surname
	    
	def get_name(self):
		return self.name
	
	def get_surname(self):
		return self.surname

class Employee(User):
	def __init__(self,age, salary):
		self.age = age
		self.salary = salary