
class schoolMember:
    def __init__(self,name):
        self.name=name
    def tell(self):
        print('hi school member:', self.name,end=" ")

# If subclass does not contain a constructor
# The subclass will have a default call to the base constructor
class Teacher(schoolMember):
    def tell(self):
        schoolMember.tell(self)
        print('and teacher')

m=Teacher('Raya')
m.tell()