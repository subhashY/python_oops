# Static and Class Methods

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

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp_1 = Employee('Subhash','Y', 50000)
emp_2 = Employee('Princ','Kumar',60000)

# Employee.set_raise_amt(10)
#
# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)


import datetime
my_date = datetime.date(2018, 8, 10)
print(Employee.is_workday(my_date))
