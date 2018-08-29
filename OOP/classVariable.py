# Class Variable

class Employee:

    no_of_emp = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@gmail.com"

        Employee.no_of_emp += 1

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('Subhash','Y', 50000)
emp_2 = Employee('Princ','Kumar',60000)

print(Employee.no_of_emp)

print(Employee.__dict__)
