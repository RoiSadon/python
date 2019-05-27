
# declare class:
class Person:
    # self - points to the current instance
    # when we call the function - the self gets the object that called him
    # so we do not need to send this parameter
    def say_hi(self):
        print("hi",self)

#Create an instance of the class
p1 = Person()
p1.say_hi()

#Create an instance of the class
p2 = Person()
p2.say_hi()

#Create a new pointer to an existing instance
p3 = p2
p3.say_hi()

#Create an instance of the class an directly execute with it the function 
(Person()).say_hi()