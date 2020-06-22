import math
import os
import random
import time
from tkinter import *
from math import *
from tkinter.messagebox import showinfo
frame = Frame(width=1000, height=800)
frame.pack()
canvas = Canvas(frame, width=800, height=800, bg='forest green', highlightthickness=0)
canvas.pack(side='left')
canvas2 = Canvas(frame, width=200, height=800, bg='khaki2', highlightthickness=0)
canvas2.pack(side='right')


def isValidMove(board, tile, ystart, xstart):
    # Checks if the move is on the board and if there is no stone already on that spot
    if (xstart > 7 or xstart < 0) or (ystart > 7 or ystart < 0):
        return False, []
    elif board[ystart][xstart] != '.':
        return False, []

    # Calculates which stones will be changed by doing said move in every possible direction
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
    # Checks if stones will be changed by doing the move and returns the stones that will be changed
    if True in check:
        return True, allchange
    else:
        return False, allchange


def allPossibilities(board, player):
    # Checks all possible moves a player has on the board
    posibilities = []
    for y in range(8):
        for x in range(8):
            if isValidMove(board, player, y, x)[0]:
                posibilities.append((y, x))
    return posibilities


def boardCopy(oldboard):
    # Creates a identical copy of the given board
    newboard = [i[:] for i in oldboard]
    return newboard


def changeBoard(board, player, y, x):
    # Carrys out all changes done by the given move
    changes = isValidMove(board, player, y, x)
    board[y][x] = player
    for i in changes[1]:
        for j in i:
            board[j[0]][j[1]] = player

    return board


def playerturn(board, y, x):
    # Recieves move and changes the board accordingly
    positiey = y
    positiex = x

    board = changeBoard(board, 'X', positiey, positiex)

    return board


def countValue(board, values):
    # Gives the current board a value for the algorithm of the computer
    count = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 'O':
                count += values[i][j]
            elif board[i][j] == 'X':
                count -= values[i][j]
    return count


def alphabeta(upperbest, move, depth, maxdepth, board, values):
    # Uses alpha-beta pruning to determine which move is the best to do
    if depth % 2 == 0:
        # Simulates a move for the computer player
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
                    themove, thescore = alphabeta(bestscore, moves[i], depth + 1, maxdepth, newboard, values)
                    if thescore > bestscore:
                        bestscore = thescore
                        bestmove = moves[i]
                    if bestscore > upperbest:
                        break

                chosenscore = bestscore
                chosenmove = bestmove
    else:
        # Simulates a move for the human player
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
                    themove, thescore = alphabeta(bestscore, moves[i], depth + 1, maxdepth, newboard, values)
                    if thescore < bestscore:
                        bestscore = thescore
                        bestmove = moves[i]
                    if bestscore < upperbest:
                        break

                chosenscore = bestscore
                chosenmove = bestmove

    return chosenmove, chosenscore


def computerturn(board, values):
    # Calculates a move and changes the board accordingly
    move = alphabeta(inf, None, 0, 6, board, values)[0]
    board = changeBoard(board, 'O', move[0], move[1])
    return board


def countScore(board, player):
    # Count how many stones of the given player are on the board
    count = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == player:
                count += 1
    return count


def createBoard():
    # Initialises the visual board structure
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
    # Puts stones on the visual board based on the internal board
    for i in range(8):
        for j in range(8):
            if board[i][j] == 'X':
                canvas.create_oval(5 + 100 * j, 5 + 100 * i, 95 + 100 * j, 95 + 100 * i, fill='black', outline='gray18',
                                   width=4)
            elif board[i][j] == 'O':
                canvas.create_oval(5 + 100 * j, 5 + 100 * i, 95 + 100 * j, 95 + 100 * i, fill='white', outline='gray85',
                                   width=4)


def othello(coords):
    # Plays the next human and computer move based on the position the human clicked on on the board
    global board
    x = floor(coords.x / 100)
    y = floor(coords.y / 100)
    # print(str(x) + '|' + str(y))

    values = [[50, -8, 3, 3, 3, 3, -8, 50],
              [-8, -10, 2, 2, 2, 2, -10, -8],
              [3, 2, 1, 1, 1, 1, 2, 3],
              [3, 2, 1, 1, 1, 1, 2, 3],
              [3, 2, 1, 1, 1, 1, 2, 3],
              [3, 2, 1, 1, 1, 1, 2, 3],
              [-8, -10, 2, 2, 2, 2, -10, -8],
              [50, -8, 3, 3, 3, 3, -8, 50]]
    player = 'X'

    # print(countValue(board, values))

    state = isValidMove(board, 'X', y, x)[0]
    # print(state)
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

    if not any('.' in i for i in board) or not any('X' in i for i in board) or not any('O' in i for i in board):
        X = 0
        O = 0
        for i in board:
            X += i.count('X')
            O += i.count('O')
        if O > X:
            label1 = Label(canvas2, text='Het spel is beeindigt', width=20, height=4)
            label2 = Label(canvas2, text="Zwart heeft {} punten".format(X), width=20, height=4)
            label3 = Label(canvas2, text="Wit heeft {} punten".format(O), width=20, height=4)
            label4 = Label(canvas2, text="De winnaar is wit!".format(O), width=20, height=4)
            label1_window = canvas2.create_window(100, 200, anchor=N, window=label1)
            label2_window = canvas2.create_window(100, 300, anchor=N, window=label2)
            label3_window = canvas2.create_window(100, 400, anchor=N, window=label3)
            label4_window = canvas2.create_window(100, 500, anchor=N, window=label4)
            # showinfo("Resultaat", "Wit heeft gewonnen met {} punten!".format(O))
        elif X > O:
            label1 = Label(canvas2, text='Het spel is beeindigt', width=20, height=4)
            label2 = Label(canvas2, text="Zwart heeft {} punten".format(X), width=20, height=4)
            label3 = Label(canvas2, text="Wit heeft {} punten".format(O), width=20, height=4)
            label4 = Label(canvas2, text="De winnaar is zwart!".format(O), width=20, height=4)
            label1_window = canvas2.create_window(100, 200, anchor=N, window=label1)
            label2_window = canvas2.create_window(100, 300, anchor=N, window=label2)
            label3_window = canvas2.create_window(100, 400, anchor=N, window=label3)
            label4_window = canvas2.create_window(100, 500, anchor=N, window=label4)
            # showinfo("Resultaat", "Zwart heeft gewonnen met {} punten!".format(X))
        else:
            label1 = Label(canvas2, text='Het spel is beeindigt', width=20, height=4)
            label2 = Label(canvas2, text="Zwart heeft {} punten".format(X), width=20, height=4)
            label3 = Label(canvas2, text="Wit heeft {} punten".format(O), width=20, height=4)
            label4 = Label(canvas2, text="Het is gelijkspel!".format(O), width=20, height=4)
            label1_window = canvas2.create_window(100, 200, anchor=N, window=label1)
            label2_window = canvas2.create_window(100, 300, anchor=N, window=label2)
            label3_window = canvas2.create_window(100, 400, anchor=N, window=label3)
            label4_window = canvas2.create_window(100, 500, anchor=N, window=label4)
            # showinfo("Resultaat", "Het is gelijkspel!")

        # print(
        #     "X heeft " + str(countScore(board, 'X')) + " punten, en O heeft " + str(countScore(board, 'O')) + " punten")


def reset():  # Reset het programma
    global board
    board = [['.', '.', '.', '.', '.', '.', '.', '.'],
             ['.', '.', '.', '.', '.', '.', '.', '.'],
             ['.', '.', '.', '.', '.', '.', '.', '.'],
             ['.', '.', '.', 'X', 'O', '.', '.', '.'],
             ['.', '.', '.', 'O', 'X', '.', '.', '.'],
             ['.', '.', '.', '.', '.', '.', '.', '.'],
             ['.', '.', '.', '.', '.', '.', '.', '.'],
             ['.', '.', '.', '.', '.', '.', '.', '.']]
    canvas.delete("all")
    canvas2.delete("all")

    createBoard()
    putStones(board)
    canvas.update()

    button1 = Button(canvas2, text='Restart', command=reset, width=15, height=4)
    button1_window = canvas2.create_window(100, 10, anchor=N, window=button1)


board = [['.', '.', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', 'X', 'O', '.', '.', '.'],
         ['.', '.', '.', 'O', 'X', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.', '.']]


# board = [['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
#          ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
#          ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
#          ['X', 'X', 'X', 'X', 'O', 'X', 'X', 'X'],
#          ['X', 'X', 'X', 'O', 'X', 'X', 'X', 'X'],
#          ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
#          ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
#          ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']]

createBoard()
putStones(board)
canvas.update()

button1 = Button(canvas2, text='Restart', command=reset, width=15, height=4)
button1_window = canvas2.create_window(100, 10, anchor=N, window=button1)

canvas.bind("<Button-1>", othello)
mainloop()
