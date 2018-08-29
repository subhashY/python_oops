# Python Object-Oriented Progrmming

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+"."+last+"@gmail.com"

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('Subhash','Y', 50000)
emp_2 = Employee('Princ','Kumar',60000)
print(emp_1.email)
print(emp_2.email)
print(emp_2.fullname())
