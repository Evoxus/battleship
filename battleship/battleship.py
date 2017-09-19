from random import randint

board = []
#This builds the board of O's
for x in range(5):
    board.append(["O"] * 5)
#This cleans up the []'s and ,'s from the board
def print_board(board):
    for row in board:
        print " ".join(row)

print " "
print "Let's play Battleship!"
print "You have 4 guesses to get it right."
print_board(board)
#This defines the ship location function
def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)
#This stores that function to a variable
ship_row = random_row(board)
ship_col = random_col(board)
#This loops through the 4 turns
for turn in range(4):
    #added the minus 1 so the player can enter rows 1-5 instead of 0-4
    guess_row = int(raw_input("Guess Row:")) - 1
    guess_col = int(raw_input("Guess Column:")) - 1

    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk my battleship!"
        break #This exits the program if player wins "Breaks the loop"
    else:
        #These are the checks for invalid guesses
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print "Oops, that's not even in the ocean."
        elif(board[guess_row][guess_col] == "X"):
            print "You guessed that one already."
        else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X"
    if turn == 3:
        print "Game Over"
    if turn <= 2:
        print "Turn", turn + 1
    else:
        print "Out of turns."
    print_board(board)
