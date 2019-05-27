
class schoolMember:
    def tell(self):
        print('\nHello school member',end=" ")

class Teacher(schoolMember):
    def tell(self):
        schoolMember.tell(self)
        print('and teacher')

class Student(schoolMember):
    def tell(self):
        schoolMember.tell(self)
        print('and student')

m = schoolMember()
t=Teacher()
s=Student()

m.tell()
t.tell()
s.tell()