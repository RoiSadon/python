import random

# Function to print the board
def drawBoard(board):
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

# Function to let the player chhose his letter
def inputPlayerLetter():
    letter = ''
    while not(letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()
    # First letter is the player's choice, second is the computer's letter
    if letter == 'X':
         return ['X', 'O']
    else:
        return ['O', 'X']

# Chooce randmonally who starts first
def whoGoesFirst():
    if random.randint(0,1) == 0:
        return 'computer'
    else:
        return 'player'

# Function to return true if player wants to play again
def playAgain():
    print('Do you want to play again? (yes or no) ')
    if input().lower == 'yes':
        return True

def makeMove(board, letter, move):
    board[move] = letter


def isWinner(bo, le):
        return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top
            (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle
            (bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom
            (bo[7] == le and bo[4] == le and bo[1] == le) or # down the left side
            (bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle
            (bo[9] == le and bo[6] == le and bo[3] == le) or # down the right side
            (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
            (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal

def getBoardCopy(board):
    dupeBoard=[]
    for i in board:
        dupeBoard.append(i)
    return dupeBoard

# Return true if the chosen place is empty
def isSpaceFree(board,move):
    return board[move]==' '

# If player chice for next move is correct
def getPlayerMove(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board,int(move)):
        print('What is your next move? (1-9)')
        move = input()
    return int(move)

def chooseRandomMoveFromList(board, moveslist):
    # possibleMoves will get all options if empty:
    possibleMoves = []
    for i in moveslist:
        if isSpaceFree(board,i):
            possibleMoves.append(i)
    if(len(possibleMoves) != 0):
        return random.choice(possibleMoves)
    else:
        return None

def getComputerMove(board,computerLetter):
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    # Algorithm for AI:
    # First: check if it can win the next move:
    for i in range(1,10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy,i):
            makeMove(copy,computerLetter,i)
            if isWinner(copy,computerLetter):
                return i 
    # Check if player can win next move, and block them:
    for i in range(1,10):
        copy = getBoardCopy(board)
        if isSpaceFree(board,i):
            makeMove(copy,playerLetter,i)
            if isWinner(copy,playerLetter):
                return i
    # Try to take one of the corners if they are free:
    move = chooseRandomMoveFromList(board, [1,3,7,9])
    if move != None:
        return move 
    # Try to take the center if free:
    if isSpaceFree(board,5):
        return 5
    # Move on one of the sides:
    return chooseRandomMoveFromList(board,[2,4,6,8])

# Return true if borad is full, else false.
def isBoardFull(board):
    for i in range(1,10):
        if isSpaceFree(board,i):
            return False
    return True

print('Welcome to TIC TAC TOE game!')

while True:
    # Reset the board:
    theBoard=[' ']*10
    playerletter , computerletter = inputPlayerLetter()
    turn = whoGoesFirst()
    print( 'The '+turn+ ' will go first.')
    gameIsPlaying = True
    while gameIsPlaying:
        # Player move:
        if turn=='player':
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard,playerletter,move)
            
            if isWinner(theBoard,playerletter):
                drawBoard(theBoard)
                print('Well done! You won the game!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('the game is a tie!')
                    break
                else:
                    turn = 'computer'
        # Computer move:
        else:
            move = getComputerMove(theBoard,computerletter)
            makeMove(theBoard,computerletter,move)

            if isWinner(theBoard,computerletter):
                drawBoard(theBoard)
                print('The computer has beaten you! you lose!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player'
    if not playAgain():
        break


















































