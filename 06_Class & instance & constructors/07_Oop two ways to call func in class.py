
class SchoolMember:
    def __init__(self,name):
        self.name = name
    def tell(self):
        print('Hello School member', self.name)

m1=SchoolMember("Oz")
# First way to call func in class:
m1.tell()
# Second way to call func in class:
#SchoolMember.tell(m1)

m2=SchoolMember("tsur")
m2.tell()