
class Movie:
    def __init__(self,name,length):
        self.name = name
        self.length=length

    def print_info(self):
        return 'name: {}, length: {}'.format(self.name,self.length)