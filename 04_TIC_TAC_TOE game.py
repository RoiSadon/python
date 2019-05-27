
board = [1,2,3,4,5,6,7,8,9]
player1 = 'X'
player2 = 'O'
print("     Welcome to TIC_TAC_TO game")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(" ")
person='O'

#define user:
def user(person):
    if person == player1:
        person == player2
    else: 
        person = player1
    return person

def win(board):
    if (board[0]==board[1] and board[0]==board[2]):
        return True
    if (board[3]==board[4] and board[3]==board[5]):
        return True
    if(board[6]==board[7] and board[6]==board[8]):
        return True
    if(board[0]==board[3] and board[0]==board[6]):
        return True
    if(board[1]==board[4] and board[1]==board[7]):
        return True
    if(board[2]==board[5] and board[2]==board[8]):
        return True
    if(board[0]==board[4] and board[0]==board[8]):
        return True
    if(board[2]==board[4] and board[2]==board[6]):
        return True
    else:
        return False

def show(board):
    print ("        |",board[0], '|' , board[1], '|',  board[2], '|')
    print  ("        ","----------")
    print ("        |",board[3], '|' , board[4], '|',  board[5], '|')
    print  ("        ","----------")
    print  ("        |",board[6], '|' , board[7], '|',  board[8], '|')
    print  ("        ","----------")

def game(board,person):   
    for i in range(9): 
        show(board)  
        if person == player1:
            person = player2
        else: 
            person = player1
        print("Next move to player:", person)
        while True:
            a=int(input("Enter your next place: "))
            if a>0 or a<10:
                a-=1
                if(board[a] == 'X' or board[a]== 'O'):
                    continue
                else:
                    break      
        board[a]=person
        if(win(board)):
            show(board)
            print(person, "IS THE WINNER!!! :)")
            break

game(board,person)
