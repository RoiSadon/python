
# A class variable, counting the number of robots
class Robot:
    population=0

    def __init__(self,name):
        # A instance variable
        self.name=name

        # When this person is created, the robot adds to the population
        Robot.population +=1

print(Robot.population)

r1 = Robot("r1")
print(r1.name)
print(Robot.population)

r2 = Robot("R2")
print(r2.name)
print(Robot.population)