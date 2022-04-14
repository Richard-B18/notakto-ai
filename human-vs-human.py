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

board = [[i for i in range(9)]for j in range(3)]
board_i = [chr(65 + i) for i in range(3)]
moves = 0
dead_board = 0

display(board)
while True:
    # another while loop to ensure input is valid
    while True:
        choice = input('Player ' + str(2 - ((moves + 1) % 2)) + ': ')
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

    if status(board[board_choice]):
        if dead_board == 2:
            print('Player ' + str(2 - ((moves + 1) % 2)) + ' wins game')
            break
        else:
            del board[board_choice]
            del board_i[board_choice]
            dead_board += 1

    display(board)
