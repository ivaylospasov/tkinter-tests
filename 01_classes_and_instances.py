from icecream import ic

class Employee:
    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = first_name + '.' + last_name + '@company.com'

    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

employee_1 = Employee('Corey', 'Shafer', 50000)
employee_2 = Employee('John', 'Doe', 60000)

# Когато е атрибут (като pay), не се изискват скоби.
# Когато е метод (като full_name), се изискват.

ic(employee_1.pay)
ic(employee_2.pay)
ic(employee_1.full_name())
ic(employee_2.full_name())

ic(employee_1.full_name())

ic(Employee.full_name(employee_1))
