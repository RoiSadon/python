
class Cinema:
    def __init__(self):
        self.arr_halls = []
        self.arr_movies = []
        self.max_movies = 100
        self.max_halls = 6
    
    def add_hall(self,hall):
        if len(self.arr_halls) < self.max_halls:
            self.arr_halls.append(hall)
        
    def add_movie(self,movie):
        if len(self.arr_movies) < self.max_movies:
            self.arr_movies.append(movie)
        
    def order_seats(self,amount,name):
        for i in range(0,len(self.arr_halls)):
            if self.arr_halls[i].movie.name == name :
                return self.arr_halls[i].order_seats(amount)

    def print_info(self):
        seat_status="\n\n"
        for ind in range(0,len(self.arr_halls)):
            seat_status+=self.arr_halls[ind].print_info()          
            seat_status+="\n________________________________________________\n"
        return seat_status