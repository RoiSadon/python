
# Define class for halls in cinema: 
class Hall:
    def __init__(self,movie):
        # Define matrix 8/10 where all [] gets False as default. 
        self.matrix_seat = [[False for j in range(8)] for i in range(10)]
        # Movie for each hall: 
        self.movie=movie


    # Func to insert 'V' when customer buys tickets.
    # Until amount ==0 
    def order_seats(self,amount):
        for i in range(0,len(self.matrix_seat)):
            for j in range(0,len(self.matrix_seat[i])):
                # Case matrix_seat[i][j] is False: 
                if not self.matrix_seat[i][j]:
                    self.matrix_seat[i][j]=True
                    amount-=1
                    if amount==0:
                        return True
        return False

    def print_info(self):
        seat_status = "\n"
        for i in range(0,len(self.matrix_seat)):
            for j in range(0,len(self.matrix_seat[i])):
                if(self.matrix_seat[i][j]):
                    seat_status += " V |"
                else: 
                    seat_status += " X |"
            seat_status += "\n-----------------------------\n"
        # print info of movie class and hall class. 
        return self.movie.print_info() + seat_status