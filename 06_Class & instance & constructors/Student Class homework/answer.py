
# Class Student:
class Student:
    age =0
    grade=0
    sumGrades=0
    sumAges=0
    sumStudents=0

    # Constructor of class Student:
    def __init__(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade

        Student.sumGrades+=grade
        Student.sumAges+=age
        Student.sumStudents+=1

    # Divide sum of all grades in num of students.
    def avgGrades(self):
        x = self.sumGrades/Student.sumStudents
        print("Avg grades: ",x)

    # Divide sum of all ages in num of students.
    def avgAges(self):
        y = self.sumAges/Student.sumStudents
        print("Avg ages: ",y)

print("--------Welcome---------")
s1 = Student('raya',21,100)
s1.avgGrades()
s1.avgAges()
s2 = Student('raz',19,97)
s2.avgGrades()
s1.avgAges()
