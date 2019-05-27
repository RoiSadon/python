
# A class variable, counting the number of robots
class Robot:
    population=0

    def __init__(self,name):
        # A instance variable
        self.name=name
        # When this person is created, the robot adds to the population
        Robot.population +=1

    def die(self):
        print('{} is being destroyed'.format(self.name))
        Robot.population-=1
    
    def say_hi(self):
        print('Greetings, my masters are calling me {}'.format(self.name))

    @classmethod
    def how_many(class_level):
        print("We have {} Robots".format(class_level.population))

Robot.how_many()

r1 = Robot("R1")
r1.say_hi()

Robot.how_many()

r2 = Robot("R2")
r2.say_hi()

Robot.how_many()

r2.die()

Robot.how_many()
