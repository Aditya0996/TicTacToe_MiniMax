import math

import constants


def minimax(board, depth, path, alpha=float("-inf"), beta=float("inf"), point=None, myTurn=True):
    # print("Point ",point," depth ", depth)
    if point is None:
        point = (0, 0)
    if depth == constants.maxDepth or board.isFull() or board.checkWin():  # check win for both returns true false
        return finalHeuristic(board, point, depth, path), point
        # return heuristic(board,point), point

    possibleMoves = board.get_open_spaces()
    if myTurn:
        score = []
        for x in possibleMoves:
            score.append((orderHeuristic(1, board, x), x))
        score.sort(key=lambda a: a[0])
        possibleMoves = [i for (score, i) in score]
        value = float("-inf")
        for moves in possibleMoves:
            board.add_symbol((moves[0], moves[1]), 1)
            path.append(moves)
            board.isGameOver(moves, myTurn)
            newValue, newPoint = minimax(board, depth + 1, path, alpha, beta, moves, not myTurn)
            if newValue > value:
                # value, point = newValue, newPoint
                value, point = newValue, moves
            if value > alpha:
                alpha = value
            board.remove_symbol((moves[0], moves[1]))
            if alpha >= beta:
                break
    else:
        score = []
        for x in possibleMoves:
            score.append((orderHeuristic(-1, board, x), x))
        score.sort(key=lambda a: a[0])
        possibleMoves = [i for (score, i) in score]
        value = float("inf")
        for moves in possibleMoves:
            board.add_symbol((moves[0], moves[1]), -1)
            board.isGameOver(moves, myTurn)
            path.append(moves)
            newValue, newPoint = minimax(board, depth + 1, path, alpha, beta, moves, not myTurn)
            if newValue < value:
                # value, point = newValue, newPoint
                value, point = newValue, moves
            if value < beta:
                beta = value
            board.remove_symbol((moves[0], moves[1]))
            if alpha >= beta:
                break
    return value, point


def finalHeuristic(board, point, depth, path):
    dimensions = board.getDimensions()
    if board.board[point[0]][point[1]] == 1:
        turn = 1
    else:
        turn = -1
    score = 0
    target = board.getTarget()
    # pointList = []
    for rowCoord in range(0, dimensions):
        for colCoord in range(0, dimensions):
            score += getScore(board, rowCoord, colCoord, target)
    # score = getScoreNew(board, point, path)
    # for moves in path:
    #     score += getScore(board, moves[0], moves[1], target)
    if turn == 1:
        return score - depth
    else:
        return score + depth


def getScore(board, x, y, step):
    dimensions = board.getDimensions()
    count_player = 0
    count_opponent = 0
    score = 0
    rowArray = board.board[x:x + 1, y:(y + step) if y + step < dimensions else dimensions]
    # colArray = board.board[x:(x + step) if x + step < dimensions else dimensions, y:y + 1]
    colArray = []
    i = 0
    while x + i < dimensions and len(colArray) <= step:
        colArray.append(board.board[x + i][y])
        i += 1
    negativeDiagonal = []
    ndx, ndy = x, y
    count = 0
    while ndx < dimensions and ndy < dimensions and count < step:
        negativeDiagonal.append(board.board[ndx][ndy])
        ndx += 1
        ndy += 1
        count += 1
    positiveDiagonal = []
    pdx, pdy = x, y
    count = 0
    while pdx > -1 and pdy < dimensions and count < step:
        positiveDiagonal.append(board.board[pdx][pdy])
        pdx -= 1
        pdy += 1
        count += 1

    # Calculate row scores
    rowCount = 0
    rowArray = rowArray[0]
    if 1 in rowArray and -1 in rowArray:
        score += 0
    elif len(rowArray) >= step:
        for x in rowArray:
            if x == 1:
                count_player += 1
                rowCount += 1
            elif x == -1:
                rowCount -= 1
                count_opponent += 1
    # Calculate column scores
    colCount = 0
    if 1 in colArray and -1 in colArray:
        score += 0
    elif len(colArray) >= step:
        for x in colArray:
            if x == 1:
                count_player += 1
                colCount += 1
            elif x == -1:
                count_opponent += 1
                colCount -= 1
    # Calculate negative diagonal scores
    ndCount = 0
    if 1 in negativeDiagonal and -1 in negativeDiagonal:
        score += 0
    elif len(negativeDiagonal) >= step:
        for x in negativeDiagonal:
            if x == 1:
                count_player += 1
                ndCount += 1
            elif x == -1:
                count_opponent += 1
                ndCount -= 1
    # Calculate positive diagonal scores
    pdCount = 0
    if 1 in positiveDiagonal and -1 in positiveDiagonal:
        score += 0
    elif len(positiveDiagonal) >= step:
        for x in positiveDiagonal:
            if x == 1:
                count_player += 1
                pdCount += 1
            elif x == -1:
                count_opponent += 1
                pdCount -= 1
    if colCount == step or rowCount == step or ndCount == step or pdCount == step:
        return 1000
    elif colCount == -step or rowCount == -step or ndCount == -step or pdCount == -step:
        return -1000
    else:
        return count_player - count_opponent


# def getScoreNew(board, move, path):
#     score = 0
#     for moves in path:
#         x = moves[0]
#         y = moves[1]
#         if board.board[x][y] == 1:
#             score += CheckCol(x, y, board) + CheckRow(x, y, board) + CheckDiagonalFromTopLeft(x, y,
#                                                                                               board) + CheckDiagonalFromTopRight(
#                 x, y, board)
#         else:
#             score -= CheckCol(x, y, board) + CheckRow(x, y, board) + CheckDiagonalFromTopLeft(x, y,
#                                                                                               board) + CheckDiagonalFromTopRight(
#                 x, y, board)
#     if board.board[move[0]][move[1]] == 1:
#         return score
#     else:
#         return -score


def CheckCol(x, y, board):
    i = j = y
    if board.board[x][y] == 1:
        current = 1
        curOpponent = -1
    else:
        current = -1
        curOpponent = 1
    while i > -1 and board.board[x][i] == current:
        i -= 1
    while j < board.getDimensions() and board.board[x][j] == current:
        j += 1
    continuous = j - i - 1
    left1 = i
    right1 = j
    while i > -1 and board.board[x][i] != curOpponent:
        i -= 1
    while j < board.getDimensions() and board.board[x][j] != curOpponent:
        j += 1
    if j - right1 + continuous >= board.getTarget() and left1 - i + continuous >= board.getTarget():
        return 4 ** continuous
    elif j - i - 1 < board.getTarget():
        return 0
    else:
        return math.pow(4, (continuous - 1))


def CheckRow(x, y, board):
    i = j = x
    if board.board[x][y] == 1:
        current = 1
        curOpponent = -1
    else:
        current = -1
        curOpponent = 1
    while i > -1 and board.board[i][y] == current:
        i -= 1
    while j < board.getDimensions() and board.board[j][y] == current:
        j += 1
    continuous = j - i - 1
    left1 = i
    right1 = j
    while i > -1 and board.board[i][y] != curOpponent:
        i -= 1
    while j < board.getDimensions() and board.board[j][y] != curOpponent:
        j += 1
    if j - right1 + continuous >= board.getTarget() and left1 - i + continuous >= board.getTarget():
        return 4 ** continuous
    elif j - i - 1 < board.getTarget():
        return 0
    else:
        return math.pow(4, (continuous - 1))


def CheckDiagonalFromTopLeft(x, y, board):
    ix = jx = x
    iy = jy = y
    if board.board[x][y] == 1:
        current = 1
        curOpponent = -1
    else:
        current = -1
        curOpponent = 1
    while ix > -1 and iy < board.getDimensions() and board.board[ix][iy] == current:
        ix -= 1
        iy += 1
    while jx < board.getDimensions() and jy > -1 and board.board[jx][jy] == current:
        jx += 1
        jy -= 1
    continuous = jx - ix - 1
    left1 = ix
    right1 = jx
    while ix > -1 and iy < board.getDimensions() and board.board[ix][iy] != curOpponent:
        ix -= 1
        iy += 1
    while jx < board.getDimensions() and jy > -1 and board.board[jx][jy] != curOpponent:
        jx += 1
        jy -= 1
    if jx - right1 + continuous >= board.getTarget() and left1 - ix + continuous >= board.getTarget():
        return 4 ** continuous
    elif jx - ix - 1 < board.getTarget():
        return 0
    else:
        return math.pow(4, (continuous - 1))


def CheckDiagonalFromTopRight(x, y, board):
    ix = jx = x
    iy = jy = y
    if board.board[x][y] == 1:
        current = 1
        curOpponent = -1
    else:
        current = -1
        curOpponent = 1
    while ix > -1 and iy > -1 and board.board[ix][iy] == current:
        ix -= 1
        iy -= 1
    while jx < board.getDimensions() and jy < board.getDimensions() and board.board[jx][jy] == current:
        jx += 1
        jy += 1
    continuous = jx - ix - 1
    left1 = ix
    right1 = jx
    while ix > -1 and iy > -1 and board.board[ix][iy] != curOpponent:
        ix -= 1
        iy -= 1
    while jx < board.getDimensions() and jy < board.getDimensions() and board.board[jx][jy] == current:
        jx += 1
        jy += 1
    if jx - right1 + continuous >= board.getTarget() and left1 - ix + continuous >= board.getTarget():
        return 4 ** continuous
    elif jx - ix - 1 < board.getTarget():
        return 0
    else:
        return math.pow(4, (continuous - 1))


def orderHeuristic(turn, board, point):
    x = point[0]
    y = point[1]
    score = 0
    board.add_symbol((x, y), turn)
    board.isGameOver(point, True if turn == 1 else False)
    if board.checkWin():
        score += float("inf")
    else:
        score += CheckCol(x, y, board) + CheckRow(x, y, board) + CheckDiagonalFromTopLeft(x, y,
                                                                                          board) + CheckDiagonalFromTopRight(
            x, y, board)
    board.remove_symbol((x, y))
    if turn == 1:
        return score
    else:
        return -score
