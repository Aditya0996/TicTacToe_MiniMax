def random(board):
    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x] == "-":
                return str(y) + "," + str(x)
