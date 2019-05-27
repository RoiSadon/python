
class Employee:

    num_of_emps = 0
    # raise_amt of salary in 4%
    raise_amt = 1.04

    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email= first + '.' + last + '@gmail.com'

        # in every creation of instance - 
        # amount of sum emp will increase in 1
        Employee.num_of_emps +=1

    def fullname(self):
        return '{} {}'.format(self.first,self.last)

    # method to increase the salary in raise_amt
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
    
    # classmethod - will get class as first attribute. 
    # will be able to change gloabl attributes.
    @classmethod 
    def set_raise_amt(cls,amount):
        cls.raise_amt = amount
    
    @classmethod
    def from_string(cls,em_str):
        first,last,pay = em_str.split('-')
        return cls(first,last,pay)
    
    # static method - doesnt use attributes from instance or class:
    # weekday - built in func. 5/6 - shabat and sunday. 
    @staticmethod 
    def is_workday(day):
        if day.weekday() == 5 or day.weekday()==6:
            return False
        return True
    
e1=Employee('Corey','Schafer',30000)
e2=Employee('Rina','Levi',50000)

# change the raised amount. 
Employee.set_raise_amt(1.05)

print(Employee.raise_amt)
print(e1.raise_amt)
print(e2.raise_amt)


s1 = 'John-Doe-70000'
s2 = 'Steve-Smith-30000'
s3 = 'Jane-Doe-90000'

# instead of doing that: 
first, last, pay =s1.split('-')

# we can do that:
e3 = Employee.from_string(s1)

print(e3.email)

import datetime
my_date = datetime.date(2016,7,11)
print(Employee.is_workday(my_date))





