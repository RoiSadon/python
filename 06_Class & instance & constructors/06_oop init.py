
class Person:
    #__init__ is a constructor:
    def __init__(self,name):
        self.name = name
    def say_hi(self):
        print('hi', self.name)

p1 = Person("Raya")
p1.say_hi()
p2 = Person("raz")
p2.say_hi()