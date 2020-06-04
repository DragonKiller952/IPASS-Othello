import random
from tkinter import *
canvas = Canvas(width=800, height=800, bg='green', highlightthickness=0)
canvas.pack()

def isValidMove(board, tile, ystart, xstart):
    if (xstart > 7 or xstart < 0) or (ystart > 7 or ystart < 0):
        return False, []
    elif board[ystart][xstart] != '.':
        return False, []

    directions = [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]
    check = []
    allchange = []
    for i in directions:
        if (8 > xstart + i[1] > -1) and (8 > ystart + i[0] > -1):
            current = board[ystart + i[0]][xstart + i[1]]

            if current != '.' and current != tile:
                currentchange = [(ystart + i[0], xstart + i[1])]
                times = 2

                while (8 > xstart + (i[1] * times) > -1) and (8 > ystart + (i[0] * times) > -1):
                    if board[ystart + (i[0] * times)][xstart + (i[1] * times)] == '.':
                        check.append(False)
                        allchange.append([])
                        break
                    elif board[ystart + (i[0] * times)][xstart + (i[1] * times)] == tile:
                        check.append(True)
                        allchange.append(currentchange)
                        break
                    else:
                        currentchange.append((ystart + (i[0] * times), xstart + (i[1] * times)))
                        times += 1
            else:
                check.append(False)
                allchange.append([])
    if True in check:
        return True, allchange
    else:
        return False, allchange


def allPossibilities(board, player):
    posibilities = []
    for y in range(8):
        for x in range(8):
            if isValidMove(board, player, y, x)[0]:
                posibilities.append((y, x))
    return posibilities


# def boardCopy(oldboard):
#     newboard = [i[:] for i in oldboard]
#     return newboard


# def allpossBoard(board, player):
#     board2 = boardCopy(board)
#     allposs = allPossibilities(player)
#     for i in allposs:
#         board2[i[0]][i[1]] = '*'
#     return board2


def changeBoard(board, player, y, x):
    changes = isValidMove(board, player, y, x)
    board[y][x] = player
    for i in changes[1]:
        for j in i:
            board[j[0]][j[1]] = player

    return board


def playerturn(board):
    valid = False
    while not valid:
        positiex = 0
        while positiex > 8 or positiex < 1:
            try:
                positiex = int(input("Geeft de positie van x-as van 1 t/m 8: "))
            except:
                positiex = -1

        positiey = 0
        while positiey > 8 or positiey < 1:
            try:
                positiey = int(input("Geeft de positie van y-as van 1 t/m 8: "))
            except:
                positiey = -1

        if isValidMove(board, 'X', positiey - 1, positiex - 1)[0]:
            board = changeBoard(board, 'X', positiey - 1, positiex - 1)
            valid = True
        else:
            print("Dit is geen geldige zet")
    return board


def computerturn(board):
    poss = allPossibilities(board, 'O')
    move = random.choice(poss)
    board = changeBoard(board, 'O', move[0], move[1])
    return board


def countScore(board, player):
    count = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == player:
                count += 1
    return count


def countValue(board, value):
    count = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 'O':
                count += value[i][j]
            elif board[i][j] == 'X':
                count -= value[i][j]
    return count

def createBoard():
    canvas.create_line(0, 0, 0, 800, fill="dark green", width=4)
    canvas.create_line(100, 0, 100, 800, fill="dark green", width=4)
    canvas.create_line(200, 0, 200, 800, fill="dark green", width=4)
    canvas.create_line(300, 0, 300, 800, fill="dark green", width=4)
    canvas.create_line(400, 0, 400, 800, fill="dark green", width=4)
    canvas.create_line(500, 0, 500, 800, fill="dark green", width=4)
    canvas.create_line(600, 0, 600, 800, fill="dark green", width=4)
    canvas.create_line(700, 0, 700, 800, fill="dark green", width=4)
    canvas.create_line(800, 0, 800, 800, fill="dark green", width=4)

    canvas.create_line(0, 0, 800, 0, fill="dark green", width=4)
    canvas.create_line(0, 100, 800, 100, fill="dark green", width=4)
    canvas.create_line(0, 200, 800, 200, fill="dark green", width=4)
    canvas.create_line(0, 300, 800, 300, fill="dark green", width=4)
    canvas.create_line(0, 400, 800, 400, fill="dark green", width=4)
    canvas.create_line(0, 500, 800, 500, fill="dark green", width=4)
    canvas.create_line(0, 600, 800, 600, fill="dark green", width=4)
    canvas.create_line(0, 700, 800, 700, fill="dark green", width=4)
    canvas.create_line(0, 800, 800, 800, fill="dark green", width=4)

    canvas.create_window(300, 300)

def putStones(board):
    for i in range(8):
        for j in range(8):
            if board[i][j] == 'X':
                canvas.create_oval(5+100*j, 5+100*i, 95+100*j, 95+100*i, fill='black', outline='gray18', width=4)
            elif board[i][j] == 'O':
                canvas.create_oval(5+100*j, 5+100*i, 95+100*j, 95+100*i, fill='white', outline='gray85', width=4)


def othello():
    board = [['.', '.', '.', '.', '.', '.', '.', '.'],
             ['.', '.', '.', '.', '.', '.', '.', '.'],
             ['.', '.', '.', '.', '.', '.', '.', '.'],
             ['.', '.', '.', 'X', 'O', '.', '.', '.'],
             ['.', '.', '.', 'O', 'X', '.', '.', '.'],
             ['.', '.', '.', '.', '.', '.', '.', '.'],
             ['.', '.', '.', '.', '.', '.', '.', '.'],
             ['.', '.', '.', '.', '.', '.', '.', '.']]

    values = [['.', '.', '.', '.', '.', '.', '.', '.'],
              ['.', '.', '.', '.', '.', '.', '.', '.'],
              ['.', '.', '.', '.', '.', '.', '.', '.'],
              ['.', '.', '.', 'X', 'O', '.', '.', '.'],
              ['.', '.', '.', 'O', 'X', '.', '.', '.'],
              ['.', '.', '.', '.', '.', '.', '.', '.'],
              ['.', '.', '.', '.', '.', '.', '.', '.'],
              ['.', '.', '.', '.', '.', '.', '.', '.']]
    player = 'X'
    print('*  -  -  -  -  -  -  -  -  *\n|  {}  |\n*  -  -  -  -  -  -  -  -  *'
          .format('  |\n|  '.join(map('  '.join, board))))

    createBoard()
    canvas.update()

    # while any('.' in i for i in board):
    for i in range(5):
        print("X heeft "+str(countScore(board, 'X'))+" punten, en O heeft "+str(countScore(board, 'O'))+" punten")
        if player == 'X':
            if allPossibilities(board, player):
                board = playerturn(board)
            player = 'O'
        else:
            if allPossibilities(board, player):
                board = computerturn(board)
            player = 'X'
        print('*  -  -  -  -  -  -  -  -  *\n|  {}  |\n*  -  -  -  -  -  -  -  -  *'
              .format('  |\n|  '.join(map('  '.join, board))))
        putStones(board)
        canvas.update()

    print('*  -  -  -  -  -  -  -  -  *\n|  {}  |\n*  -  -  -  -  -  -  -  -  *'
          .format('  |\n|  '.join(map('  '.join, board))))
    print("X heeft " + str(countScore(board, 'X')) + " punten, en O heeft " + str(countScore(board, 'O')) + " punten")


othello()
mainloop()
# print('*  -  -  -  -  -  -  -  -  *\n|  {}  |\n*  -  -  -  -  -  -  -  -  *'
#       .format('  |\n|  '.join(map('  '.join, board2))))




