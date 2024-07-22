import datetime


class Employee:
    raise_amount = 1.04

    def __init__(self, first_name, last_name, pay):
        self.first = first_name
        self.last = last_name
        self.pay = pay

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        firstname, lastname = name.split(' ')
        self.first = firstname
        self.last = lastname

    @fullname.deleter
    def fullname(self):
        print('Deleted Name!:{}'.format(self.fullname))
        self.first = None
        self.last = None

    def apply_raise(self):
        self.pay = self.pay * self.raise_amount

    def __repr__(self):
        return "Employee('{}','{}','{}')".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname, self.email)

    def __add__(self, other):
        return self.pay + other.pay

    # def __len__(self):
    #     return len(self.fullname())

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, employee_string):
        first, last, pay = employee_string.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first_name, last_name, pay, prog_lang):
        super().__init__(first_name, last_name, pay)
        self.prog_lang = prog_lang


class Manager(Employee):
    def __init__(self, first_name, last_name, pay, employees=None):
        super().__init__(first_name, last_name, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def delete_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print('-->', emp.fullname)


