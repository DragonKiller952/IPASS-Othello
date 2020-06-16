import math
import random
import time
from tkinter import *
from math import *
from tkinter.messagebox import showinfo

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


def boardCopy(oldboard):
    newboard = [i[:] for i in oldboard]
    return newboard


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


def playerturn(board, y, x):
    positiey = y
    positiex = x

    board = changeBoard(board, 'X', positiey, positiex)

    return board


def countValue(board, values):
    count = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 'O':
                count += values[i][j]
            elif board[i][j] == 'X':
                count -= values[i][j]
    return count


def minimax( move, depth, maxdepth, board, values):
    if depth % 2 == 0:
        if depth == maxdepth:
            chosenscore = countValue(board, values)
            chosenmove = move
        else:
            moves = allPossibilities(board, 'O')
            if not moves:
                chosenscore = countValue(board, values)
                chosenmove = move
            else:
                bestscore = -inf
                for i in range(len(moves)):
                    newboard = boardCopy(board)
                    changeBoard(newboard, 'O', moves[i][0], moves[i][1])
                    themove, thescore = minimax(moves[i], depth+1, maxdepth, newboard, values)
                    if thescore>bestscore:
                        bestscore = thescore
                        bestmove = moves[i]

                chosenscore = bestscore
                chosenmove = bestmove
    else:
        if depth == maxdepth:
            chosenscore = countValue(board, values)
            chosenmove = move
        else:
            moves = allPossibilities(board, 'X')
            if not moves:
                chosenscore = countValue(board, values)
                chosenmove = move
            else:
                bestscore = inf
                for i in range(len(moves)):
                    newboard = boardCopy(board)
                    changeBoard(newboard, 'X', moves[i][0], moves[i][1])
                    themove, thescore = minimax(moves[i], depth + 1, maxdepth, newboard, values)
                    if thescore < bestscore:
                        bestscore = thescore
                        bestmove = moves[i]

                chosenscore = bestscore
                chosenmove = bestmove

    return chosenmove, chosenscore


def computerturn(board, values):
    poss = allPossibilities(board, 'O')
    # move = random.choice(poss)
    move = minimax(None, 0, 6, board, values)[0]
    board = changeBoard(board, 'O', move[0], move[1])
    return board


def countScore(board, player):
    count = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == player:
                count += 1
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
                canvas.create_oval(5 + 100 * j, 5 + 100 * i, 95 + 100 * j, 95 + 100 * i, fill='black', outline='gray18',
                                   width=4)
            elif board[i][j] == 'O':
                canvas.create_oval(5 + 100 * j, 5 + 100 * i, 95 + 100 * j, 95 + 100 * i, fill='white', outline='gray85',
                                   width=4)


def othello(coords):
    global board
    x = floor(coords.x / 100)
    y = floor(coords.y / 100)
    print(str(x) + '|' + str(y))

    values = [[8, -8, 3, 3, 3, 3, -8, 8],
              [-8, -10, 2, 2, 2, 2, -10, -8],
              [3, 2, 1, 1, 1, 1, 2, 3],
              [3, 2, 1, 1, 1, 1, 2, 3],
              [3, 2, 1, 1, 1, 1, 2, 3],
              [3, 2, 1, 1, 1, 1, 2, 3],
              [-8, -10, 2, 2, 2, 2, -10, -8],
              [8, -8, 3, 3, 3, 3, -8, 8]]
    player = 'X'

    print(countValue(board, values))

    state = isValidMove(board, 'X', y, x)[0]
    print(state)
    if allPossibilities(board, 'X'):
        if allPossibilities(board, player) and state:
            board = playerturn(board, y, x)
        canvas.delete("all")
        createBoard()
        putStones(board)
        canvas.update()
        time.sleep(0.5)
        player = 'O'
        if allPossibilities(board, player) and state:
            board = computerturn(board, values)
        canvas.delete("all")
        createBoard()
        putStones(board)
    else:
        if allPossibilities(board, 'O'):
            board = computerturn(board, values)
        canvas.delete("all")
        createBoard()
        putStones(board)

    if not any('.' in i for i in board):
        X = 0
        O = 0
        for i in board:
            X += i.count('X')
            O += i.count('O')

        if O>X:
            showinfo("Resultaat", "Wit heeft gewonnen met {} punten!".format(O))
        elif X>O:
            showinfo("Resultaat", "Zwart heeft gewonnen met {} punten!".format(X))
        else:
            showinfo("Resultaat", "Het is gelijkspel!")

        print(
            "X heeft " + str(countScore(board, 'X')) + " punten, en O heeft " + str(countScore(board, 'O')) + " punten")



board = [['.', '.', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', 'X', 'O', '.', '.', '.'],
         ['.', '.', '.', 'O', 'X', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '.']]

createBoard()
putStones(board)
canvas.update()


canvas.bind("<Button-1>", othello)
mainloop()
