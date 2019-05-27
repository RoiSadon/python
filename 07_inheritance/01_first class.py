
# Basic class: 

class Employee:

    # init - constructor of the class Employee
    # always gets self as first parameter. 
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        # Declare Email for each instance using given data
        # and concatenation
        self.email = first + '.' + last + '@gmail.com'

    #method to return Employee full name
    def fullname(self):
        return '{} {}'.format(self.first,self.last)

# two instances using init constructor:
e1 = Employee('Raya','Hazi',50000)
e2 = Employee('Raz','Cohen',45000)

# call method or attribute:
# if method - () in the end.
print(e1.fullname())
print(e2.email)