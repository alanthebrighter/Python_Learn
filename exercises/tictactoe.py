import random

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    row1 = board[0]
    row2 = board[1]
    row3 = board[2]
    fixLine = '+-------+-------+-------+'
    
    print(fixLine)

    for row in board:
        print("|       |       |       |")
        print(f"|   {row[0]}   |   {row[1]}   |   {row[2]}   |")
        print("|       |       |       |")
        print(fixLine)

def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    
    while True:
        try:
            userInput = int(input("Enter your position: ")) - 1
            if (userInput >= 0 and userInput < 9):
                r = userInput // 3
                c = userInput % 3
                if(str(board[r][c]) not in "XO"):
                    board[r][c] = "O"
                    #display_board(board)
                    break
                else:
                    print("Not available")
            else:
                print("position not valid")
        except ValueError:
            print("Enter a valid integer!")
         

def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free_fields = []
    for r in range(3):
        for c in range(3):
            if str(board[r][c]) not in "XO":
                free_fields.append((r, c))
                
    return free_fields

def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    if board[0][0] == sign and board[0][1] == sign and board[0][2] == sign:
        return True
    elif board[1][0] == sign and board[1][1] == sign and board[1][2] == sign:
        return True
    elif board[2][0] == sign and board[2][1] == sign and board[2][2] == sign:
        return True
    elif board[0][0] == sign and board[1][0] == sign and board[2][0] == sign:
        return True
    elif board[0][1] == sign and board[1][1] == sign and board[2][1] == sign:
        return True
    elif board[0][2] == sign and board[1][2] == sign and board[2][2] == sign:
        return True
    elif board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        return True
    elif board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:
        return True
    else:
        return False 


def draw_move(board):
    # The function draws the computer's move and updates the board.
    print("Computer is playing...")
    computerChoice = random.choice(make_list_of_free_fields(board))
    board[computerChoice[0]][computerChoice[1]] = "X"

wantToPlay = input("Do you want to play?").lower()
while wantToPlay == "y":
    computer = "X"
    user = "O"

    board = [[1, 2, 3,],[4, 'X', 6],[7, 8, 9]]
    display_board(board)

    while True:
        enter_move(board)
        display_board(board)
        if(victory_for(board, user)):
            print("Congratulation, You win!")
            break
        elif(victory_for(board, user) == False and len(make_list_of_free_fields(board)) == 0):
            print("Draw!")
            break
        else:
            draw_move(board)
            display_board(board)
            if(victory_for(board, computer)):
                print("Sorry! You lose! Computer Won!")
                break
            elif(victory_for(board, computer) == False and len(make_list_of_free_fields(board)) == 0):
                print("Draw!")
                break

    wantToPlay = input("Do you want to play again? y/n: ")

print("Goodbye!")
