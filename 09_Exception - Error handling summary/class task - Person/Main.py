from Person_class import Person
import random

# create an empty array with 5 empty cales:
arr_people = [0,0,0,0,0]

# given arrays:
arr_names=["Tom", "li" , "Bob" , "Alice" , "Clarc" , "Adam" , "Sean"]
arr_eye_colors=["green", "blue" , "yellow" , "black" ]

# for loop to insert data of 5 Person instances. 
# the data will be inserted until it will be valid!
for i in range(len(arr_people)):
   # set age:
    a = random.randrange(-20,200)
    while a<0 or a>120:
        a = random.randrange(-20,200)
    arr_people[i]=Person().set_age(a)  
    
    # set name:
    n = random.choice(arr_names)
    while len(n)<3 or len(n)>9:
        n = random.choice(arr_names)
    arr_people[i] = Person().set_name(n)

    # set eye_color:
    e = random.choice(arr_eye_colors)
    while e != "green" and e!="blue" and e!="brown":
        e = random.choice(arr_eye_colors)
    arr_people[i]=Person().set_eye_color(e)

