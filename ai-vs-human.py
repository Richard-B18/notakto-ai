def display(board):
    for i in range(len(board)):
        if i != len(board) - 1:
            print(f'{board_i[i]:<6}', end = ' ')
        else:
            print(board_i[i])
    for i in range(3):
        for j in range(len(board) * 3):
            if (j + 1) % 3 == 0 and (j + 1) // 3 != len(board):
                print(board[j // 3][i * 3 + j % 3], end = '  ')
            elif (j + 1) // 3 == 3:
                print(board[j // 3][i * 3 + j % 3], end= '')
            else:
                print(board[j // 3][i * 3 + j % 3], end= ' ')
        print()

def status(board):
    count_r = 0
    count_c = 0
    count_d1 = 0
    count_d2 = 0
    for i in range(3):
        count_r = 0
        count_c = 0
        for j in range(3):
            if board[i * 3 + j] == 'X':
                count_c += 1
            if board[i + j * 3] == 'X':
                count_r += 1
        if count_c == 3 or count_r == 3:
            return True
        if board[2 * (i + 1)] == 'X':
            count_d2 += 1
        if board[4 * i] == 'X':
            count_d1 += 1
    if count_d1 == 3 or count_d2 == 3:
        return True
    return False

def possibleMoves(board):
    possible = []
    testBoard = board[:]
    for i in range(len(testBoard)):
        for j in range(9):
            if testBoard[i][j] != 'X':
                possible.append(board_i[i] + str(j))
    return possible
def rotate90(temp_board):
    board = [i for i in range(9)]
    board[4] = temp_board[4]
    if temp_board[0] == 'X':
        board[2] = temp_board[0]
    if temp_board[1] == 'X':
        board[5] = temp_board[1]
    if temp_board[2] == 'X':
        board[8] = temp_board[2]
    if temp_board[5] == 'X':
        board[7] = temp_board[5]
    if temp_board[8] == 'X':
        board[6] = temp_board[8]
    if temp_board[7] == 'X':
        board[3] = temp_board[7]
    if temp_board[6] == 'X':
        board[0] = temp_board[6]
    if temp_board[3] == 'X':
        board[1] = temp_board[3]
    return board

def flipH(temp_board):
    board = [i for i in range(9)]
    for i in range(1,8,3):
        board[i] = temp_board[i]
    for i in range(0,7,3):
        if temp_board[2 + i] == 'X':
            board[i] = temp_board[2 + i]
        if temp_board[i] == 'X':
            board[2 + i] = temp_board[i]
    return board

def flipV(temp_board):
    board = [i for i in range(9)]
    for i in range(3,6):
        board[i] = temp_board[i]
    for i in range(3):
        if temp_board[i] == 'X':
            board[6 + i] = temp_board[i]
        if temp_board[6 + i] == 'X':
            board[i] = temp_board[6 + i]
    return board

def position(board):
    for i in range(3):
        if i != 0:
            if i == 1:
                board = flipH(board)
            else:
                board = flipV(board)
        for j in range(4):
            if j != 0:
                board = rotate90(board)
            if board == [0, 1, 2, 3, 4, 5, 6, 7, 8]:
                return c
            elif board == [0, 1, 2, 3, 'X', 5, 6, 7, 8]:
                return c ** 2
            elif board == ['X', 'X', 2, 3, 4, 5, 6, 7, 8]:
                return a * d
            elif board == ['X', 1, 'X', 3, 4, 5, 6, 7, 8]:
                return b
            elif board == ['X', 1, 2, 3, 'X', 5, 6, 7, 8]:
                return b
            elif board == ['X', 1, 2, 3, 4, 'X', 6, 7, 8]:
                return b
            elif board == ['X', 1, 2, 3, 4, 5, 6, 7, 'X']:
                return a
            elif board == [0, 'X', 2, 'X', 4, 5, 6, 7, 8]:
                return a
            elif board == [0, 'X', 2, 3, 'X', 5, 6, 7, 8]:
                return b
            elif board == [0, 'X', 2, 3, 4, 5, 6, 'X', 8]:
                return a
            elif board == ['X', 'X', 2, 'X', 4, 5, 6, 7, 8]:
                return b
            elif board == ['X', 'X', 2, 3, 'X', 5, 6, 7, 8]:
                return a * b
            elif board == ['X', 'X', 2, 3, 4, 'X', 6, 7, 8]:
                return d
            elif board == ['X', 'X', 2, 3, 4, 5, 'X', 7, 8]:
                return a
            elif board == ['X', 'X', 2, 3, 4, 5, 6, 'X', 8]:
                return d
            elif board == ['X', 'X', 2, 3, 4, 5, 6, 7, 'X']:
                return d
            elif board == ['X', 1, 'X', 3, 'X', 5, 6, 7, 8]:
                return a
            elif board == ['X', 1, 'X', 3, 4, 5, 'X', 7, 8]:
                return a * b
            elif board == ['X', 1, 'X', 3, 4, 5, 6, 'X', 8]:
                return a
            elif board == ['X', 1, 2, 3, 'X', 'X', 6, 7, 8]:
                return a
            elif board == [0, 'X', 2, 'X', 'X', 5, 6, 7, 8]:
                return a * b
            elif board == [0, 'X', 2, 'X', 4, 'X', 6, 7, 8]:
                return b
            elif board == ['X', 'X', 2, 'X', 'X', 5, 6, 7, 8]:
                return a
            elif board == ['X', 'X', 2, 'X', 4, 'X', 6, 7, 8]:
                return a
            elif board == ['X', 'X', 2, 'X', 4, 5, 6, 7, 'X']:
                return a
            elif board == ['X', 'X', 2, 3, 'X', 'X', 6, 7, 8]:
                return b
            elif board == ['X', 'X', 2, 3, 'X', 5, 'X', 7, 8]:
                return b
            elif board == ['X', 'X', 2, 3, 4, 'X', 'X', 7, 8]:
                return b
            elif board == ['X', 'X', 2, 3, 4, 'X', 6, 'X', 8]:
                return a * b
            elif board == ['X', 'X', 2, 3, 4, 'X', 6, 7, 'X']:
                return a * b
            elif board == ['X', 'X', 2, 3, 4, 5, 'X', 'X', 8]:
                return b
            elif board == ['X', 'X', 2, 3, 4, 5, 'X', 7, 'X']:
                return b
            elif board == ['X', 'X', 2, 3, 4, 5, 6, 'X', 'X']:
                return a
            elif board == ['X', 1, 'X', 3, 'X', 5, 6, 'X', 8]:
                return b
            elif board == ['X', 1, 'X', 3, 4, 5, 'X', 7, 'X']:
                return a
            elif board == ['X', 1, 2, 3, 'X', 'X', 6, 'X', 8]:
                return b
            elif board == [0, 'X', 2, 'X', 4, 'X', 6, 'X', 8]:
                return a
            elif board == ['X', 'X', 2, 'X', 4, 'X', 6, 'X', 8]:
                return b
            elif board == ['X', 'X', 2, 'X', 4, 'X', 6, 7, 'X']:
                return b
            elif board == ['X', 'X', 2, 3, 'X', 'X', 'X', 7, 8]:
                return a
            elif board == ['X', 'X', 2, 3, 4, 'X', 'X', 'X', 8]:
                return a
            elif board == ['X', 'X', 2, 3, 4, 'X', 'X', 7, 'X']:
                return a
            elif board == ['X', 'X', 2, 'X', 4, 'X', 6, 'X', 'X']:
                return a
    return 1

def botMove(board):
    testBoard = board[:]
    possible = possibleMoves(testBoard)
    for i in range(len(possible)):
        product = 1
        testBoard = board[:]
        # finding the board
        for j in range(len(board_i)):
            if board_i[j] == possible[i][0]:
                board_choice = j
                break
        testBoard[board_choice][int(possible[i][1])] = 'X'
        for k in range(len(testBoard)):
            product *= position(testBoard[k])
        board[board_choice][int(possible[i][1])] = int(possible[i][1])
        if product in [c ** 2, a, b ** 2, b * c]:
            return possible[i]

board = [[i for i in range(9)]for j in range(3)]
board_i = [chr(65 + i) for i in range(3)]
moves = 0
dead_board = 0

a = 2
b = 3
c = 5
d = 7

display(board)
while True:
    if moves % 2 == 1:
        while True:
            choice = input('Player 2: ')
            for i in range(len(board_i)):
                if board_i[i] == choice[0]:
                    board_choice = i
                    break
            if len(choice) == 2 and choice[0] in board_i and int(choice[1]) <= 8:
                if board[board_choice][int(choice[1])] != 'X':
                    board[board_choice][int(choice[1])] = 'X'
                    moves += 1
                    break
                else:
                    print('Invalid move, please input again')
            else:
                print('Invalid move, please input again')
    else:
        bot = botMove(board)
        print('Player 1: ' + bot)
        for i in range(len(board_i)):
            if board_i[i] == bot[0]:
                board_choice = i
                break
        board[board_choice][int(bot[1])] = 'X'
        moves += 1
    if status(board[board_choice]):
        if dead_board == 2:
            print('Player ' + str(2 - ((moves + 1) % 2)) + ' wins game')
            break
        else:
            del board[board_choice]
            del board_i[board_choice]
            dead_board += 1
    display(board)
