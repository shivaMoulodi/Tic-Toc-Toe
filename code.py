# Initial values
player = 'o'
computer = 'x'
counter_minimax = 0
board = {1:'_', 2: '_', 3: '_',
         4:'_', 5: '_', 6: '_',
         7:'_', 8: '_', 9: '_'}

def print_board(board):
    print(board[1] + ' ' + board[2] + ' ' + board[3])
    print(board[4] + ' ' + board[5] + ' ' + board[6])
    print(board[7] + ' ' + board[8] + ' ' + board[9])
    print('\n')

def is_empty(position):
    if board[position] == '_':
        return True
    return False

def check_draw():
    for key in board.keys():
        if board[key] == '_':
            return False
    return True

def check_win():
    if board[1]==board[2] and board[1]==board[3] and board[1]!='_':
        return True
    elif board[4]==board[5] and board[4]==board[6] and board[4]!='_':
        return True
    elif board[7]==board[8] and board[8]==board[9] and board[7]!='_':
        return True
    elif board[1]==board[4] and board[1]==board[7] and board[1]!='_':
        return True
    elif board[2]==board[5] and board[2]==board[8] and board[2]!='_':
        return True
    elif board[3]==board[6] and board[3]==board[9] and board[3]!='_':
        return True
    elif board[1]==board[5] and board[1]==board[9] and board[1]!='_':
        return True
    elif board[3]==board[5] and board[3]==board[7] and board[3]!='_':
        return True
    else:
        return False
    
def check_who_win(mark):
    if board[1]==board[2] and board[1]==board[3] and board[1]==mark:
        return True
    elif board[4]==board[5] and board[4]==board[6] and board[4]==mark:
        return True
    elif board[7]==board[8] and board[8]==board[9] and board[7]==mark:
        return True
    elif board[1]==board[4] and board[1]==board[7] and board[1]==mark:
        return True
    elif board[2]==board[5] and board[2]==board[8] and board[2]==mark:
        return True
    elif board[3]==board[6] and board[3]==board[9] and board[3]==mark:
        return True
    elif board[1]==board[5] and board[1]==board[9] and board[1]==mark:
        return True
    elif board[3]==board[5] and board[3]==board[7] and board[3]==mark:
        return True
    else:
        return False

def insert(char, position):
    if is_empty(position):
        board[position] = char
        print_board(board)
        if check_draw():
            print("Draw")
            return
            
        if check_win():
            if char == 'x':
                print("you lose")
                return True
            else:
                print("you wins")
                return True
        return False
        
    else:
        position = int(input("it's full!"+'\n'+" Enter position: "))
        insert(char, position)
        print_board(board)
        return

def player_move():
    position = int(input("Please Enter your position for 'o': "))
    insert(player, position)
    return

def computer_move():
    best_score = -1000
    best_move = 0
    for key in board.keys():
        if board[key] == '_':
            board[key] = computer
            score = minimax(board, False)
            board[key] = "_"
            if (score > best_score):
                best_score = score
                best_move = key
    insert(computer, best_move)
    return

def minimax(board, isMaximizing):
    global counter_minimax
    counter_minimax = counter_minimax + 1
    
    if check_who_win(computer):
        return 1
    elif check_who_win(player):
        return -1
    elif check_draw():
        return 0
    
    if isMaximizing:
        bestScore = -1000
        for key in board.keys():
            if board[key] == '_':
                board[key] = computer
                score = minimax(board, False)
                board[key] = '_'
                if score > bestScore:
                    bestScore = score
        return bestScore

    else:
        bestScore = 1000
        for key in board.keys():
            if board[key] == '_':
                board[key] = player
                score = minimax(board, True)
                board[key] = '_'
                if score < bestScore:
                    bestScore = score
        return bestScore
    
# Main loop 
while not check_win():
    computer_move()
    res = check_win()
    d = check_draw()
    if res or d:
        break
    else:
        player_move()
        
print('counter_minimax: ', counter_minimax)
