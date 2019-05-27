
class schoolMember:
    def __init__(self,name):
        self.name=name
    def tell(self):
        print('\nhi school member:', self.name,end=" ")

# If subclass does not contain a constructor
# The subclass will have a default call to the base constructor
class Teacher(schoolMember):

    def __init__(self,name,salary):
        schoolMember.__init__(self,name)
        self.salary=salary
        
    def tell(self):
        schoolMember.tell(self)
        print('and teacher',self.salary)

a=schoolMember('Oz')
b=Teacher('Raya',10000)
a.tell()
b.tell()