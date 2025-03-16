"""
https://youtu.be/BJ-VvGyQxho?si=n8AZlZf7zPwgBv63
"""

from icecream import ic

class Employee:

    number_of_employees = 0
    raise_amount = 1.04

    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = first_name + '.' + last_name + '@company.com'

        Employee.number_of_employees += 1

    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

# Преди създаване на служителите
ic(Employee.number_of_employees)

employee_1 = Employee('Corey', 'Shafer', 50000)
employee_2 = Employee('John', 'Doe', 60000)

# Задаваме нова стойност на променливата в класа Employee за всички инстанции
# Employee.raise_amount = 1.05

# Задаваме нова стойност на променливата в класа Employee за инстанцията employee_1
# employee_1.raise_amount = 1.05
#
# ic(Employee.raise_amount)
# ic(employee_1.raise_amount)
# ic(employee_2.raise_amount)

# ic(employee_1.__dict__)

# ic(Employee.__dict__)

# След създаване на служителите
ic(Employee.number_of_employees)