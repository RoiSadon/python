
# We import the 3 files here: 
# we declare one cinema, 2 movies, 2 halls. 
# we call to orders: 

import movie
import hall
import cinema

my_cinema = cinema.Cinema()

movie1 = movie.Movie("Avatar",150)
movie2 = movie.Movie("Spiderman", 200)

hall1 = hall.Hall(movie1)
hall2 = hall.Hall(movie2)

my_cinema.add_hall(hall1)
my_cinema.add_hall(hall2)

my_cinema.order_seats(4,"Avatar")
my_cinema.order_seats(6,"Spiderman")

print(my_cinema.print_info())
