board = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
     [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
     [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
     [' ', ' ', ' ', 'X', 'O', ' ', ' ', ' '],
     [' ', ' ', ' ', 'O', 'X', ' ', ' ', ' '],
     [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
     [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
     [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]

values = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
     [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
     [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
     [' ', ' ', ' ', 'X', 'O', ' ', ' ', ' '],
     [' ', ' ', ' ', 'O', 'X', ' ', ' ', ' '],
     [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
     [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
     [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]


def isValidMove(board, tile, ystart, xstart):
    if (xstart > 7 or xstart < 0) or (ystart > 7 or ystart < 0):
        return False, []
    elif board[ystart][xstart] != ' ':
        return False, []

    directions = [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]
    check = []
    allchange = []
    for i in directions:
        if (8 > xstart + i[1] > -1) and (8 > ystart + i[0] > -1):
            current = board[ystart + i[0]][xstart + i[1]]

            if current != ' ' and current != tile:
                currentchange = [(ystart + i[0], xstart + i[1])]
                times = 2

                while (8 > xstart + (i[1] * times) > -1) and (8 > ystart + (i[0] * times) > -1):
                    if board[ystart + (i[0] * times)][xstart + (i[1] * times)] == ' ':
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


player = 'X'
newboard = [i[:] for i in board]

posibilities = []
for y in range(8):
    for x in range(8):
        if isValidMove(board, player, y, x)[0]:
            posibilities.append((y, x))
print(posibilities)
for i in posibilities:
    newboard[i[0]][i[1]] = '*'

# changes = isValidMove(a, player, y, x)
#
# if not changes[0]:
#     print("Dit is geen geldige zet")
# else:
#     newboard[y][x] = player
#     for i in changes[1]:
#         for j in i:
#             newboard[j[0]][j[1]] = player
#
print('*  -  -  -  -  -  -  -  -  *\n|  {}  |\n*  -  -  -  -  -  -  -  -  *'
      .format('  |\n|  '.join(map('  '.join, board))))

print('*  -  -  -  -  -  -  -  -  *\n|  {}  |\n*  -  -  -  -  -  -  -  -  *'
      .format('  |\n|  '.join(map('  '.join, newboard))))

