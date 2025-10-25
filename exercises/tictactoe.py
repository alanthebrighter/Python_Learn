computer = "X"
user = "O"

board = [[1, 2, 3,],[4, 'X', 6],[7, 8, 9]]


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
                    display_board(board)
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
    return None


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    return None


def draw_move(board):
    # The function draws the computer's move and updates the board.
    return None

display_board(board)
enter_move(board)
