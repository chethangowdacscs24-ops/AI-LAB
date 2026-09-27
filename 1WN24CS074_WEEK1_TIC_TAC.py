board = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}

win_conditions = [(1, 2, 3), (4, 5, 6), (7, 8, 9),  # Horizontal
                  (1, 4, 7), (2, 5, 8), (3, 6, 9),  # Vertical
                  (1, 5, 9), (3, 5, 7)]             # Diagonal

player = 'O'
bot = 'X'


def printBoard(board):
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[7] + '|' + board[8] + '|' + board[9])
    print()


def spaceFree(pos):
    return board[pos] == ' '


def checkWin():
    for a, b, c in win_conditions:
        if board[a] == board[b] == board[c] and board[a] != ' ':
            return True
    return False


def checkDraw():
    return all(board[key] != ' ' for key in board.keys())


def insertLetter(letter, position):
    if not spaceFree(position):
        position = int(input('Position taken. Enter new position: '))
        return insertLetter(letter, position)

    board[position] = letter
    printBoard(board)

    if checkWin():
        print('Bot wins!' if letter == bot else 'You win!')
        return True
    elif checkDraw():
        print('Draw!')
        return True
    return False


def findWinningMove(mark):
    # Returns a position that completes a line for 'mark', or None.
    # This is plain rule-checking, not a search algorithm: for each
    # empty cell we just check whether placing 'mark' there finishes
    # one of the fixed win_conditions.
    for pos in board:
        if board[pos] == ' ':
            board[pos] = mark          # try the move
            won = checkWin()
            board[pos] = ' '           # undo the move
            if won:
                return pos
    return None


def compMove():
    # 1. Win now if possible.
    move = findWinningMove(bot)
    # 2. Otherwise block the player's winning move.
    if move is None:
        move = findWinningMove(player)
    # 3. Otherwise prefer the center, then a corner, then any free cell.
    if move is None:
        for pos in [5, 1, 3, 7, 9, 2, 4, 6, 8]:
            if board[pos] == ' ':
                move = pos
                break

    return insertLetter(bot, move)


def playerMove():
    position = int(input('Enter position for O (1-9): '))
    return insertLetter(player, position)


game_over = False
while not game_over:
    game_over = playerMove()
    if not game_over:
        game_over = compMove()
