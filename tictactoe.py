board = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
         ]

turn = 0
def print_board(board):
    for row in board :
        for slot in row:
            print(slot,end=" ")
        print("\n")


# print_board(board)
user = True

def quit(user_input):
    if user_input.lower()=="q":
        print("Thanks for Playing!!!")
        return True
    else:
        return False


def bounds(user_input):
    if int(user_input)>0 and int(user_input)<10:
        return True
    else:
        print("This number is out of bound. Please enter number between 1-9 ")
        return False
def isnumeric(user_input):
    if not user_input.isnumeric():
        print("Enter valid no between 1-9")
        return False
    else:
        return True


def coordinates(user_input):
    row=int(user_input/3)
    col = user_input
    if col>2: col = int(col%3)
    return (row,col)

def istaken(coords,board):
    row = coords[0]
    col = coords[1]
    if board[row][col] != "-":
        print("This position is already taken")
        return True
    else:
        return False

def add_to_board(coords,board,active_user):
    row=coords[0]
    col = coords[1]
    board[row][col]=active_user


def current_user(user):
    if user: return "x"
    else: return "o"

def user_win(board,user):
    if check_col(board,user): return True
    if check_row(board,user): return True
    if check_diagnol(board,user): return True
    return False


def check_row(board,user):

    for row in board:
        complete_row = True
        for slot in row:
            if slot != user:
                complete_row=False
                break
        if complete_row: return True
    return False



def check_col(board,user):
    for i in range(3):
        complete_col = True
        for j in range(3):
            if board[i][j]!=user:
                complete_col= False
                break
        if complete_col: return True
    return False


def check_diagnol(board,user):
    if board[0][0]==user and board[1][1]==user and board[2][2]==user: return True
    elif board[0][2]==user and board[1][1]==user and board[2][0]==user: return True
    return False

while turn<9:
    active_user=current_user(user)
    print_board(board)
    user_input = input("Enter any value between 1-9 or enter 'q' to Quit ")
    if quit(user_input): break
    if not isnumeric(user_input):
        print("Go again and enter numeric value")
        continue
    if not bounds(user_input):
        continue
    # entries.append(user_input)
    user_input=int(user_input)-1
    cords = coordinates(user_input)
    # board[0][0]="x"
    if istaken(cords,board):
        print("Please enter at diff position")
        continue
    add_to_board(cords,board, active_user)

    if user_win(board, active_user):
        print(f"{active_user.upper()} won!!!")
        break
    turn+=1
    user = not user
    if turn == 9 : print("It's a tie!!!")









