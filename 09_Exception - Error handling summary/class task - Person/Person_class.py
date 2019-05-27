# note: there is no constructor here.
#  the data will be defined specificly in the functions 

class Person:

    # set_age function:
    def set_age(self,age):
        try: 
            if age <0 or age>120:
                raise Exception()
        except Exception:
            print ("NOT valid age!") 
        else:
            self.age = age
            print("age is: {}".format(age))
    
    # set_name function:
    def set_name(self,name):
        try: 
            if len(name) < 3 or len(name) > 9:
                raise Exception()
        except Exception:
            print ("NOT valid name!")
        else:
            self.name = name
            print("Valid name: ", name)
            
    # set_eye_color function:
    def set_eye_color(self,eye_color):
        try: 
            if eye_color != "green" and eye_color != "blue" and eye_color != "brown":
                raise Exception()
        except Exception:
            print ("NOT valid eye_color!")
        else:
            self.eye_color = eye_color
            print("Valid eye color: ", eye_color)
