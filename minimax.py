import constants


def minimax(board, depth, alpha, beta, point=None, myTurn=True):
    check = []
    # print("Point ",point," depth ", depth)
    if point is None:
        point = (0, 0)
    if depth == constants.maxDepth or board.isFull() or board.checkWin():  # check win for both returns true false
        return finalHeuristic(board, point, depth), point
        # return heuristic(board,point), point

    possibleMoves = board.get_open_spaces()
    if myTurn:
        value = float("-inf")
        for moves in possibleMoves:
            board.add_symbol((moves[0], moves[1]), 1)
            board.isGameOver(point, myTurn)
            newValue, newPoint = minimax(board, depth + 1, alpha, beta, moves, not myTurn)
            check.append((newValue, newPoint))
            if newValue > value:
                value, point = newValue, newPoint
            board.remove_symbol((moves[0], moves[1]))
    else:
        value = float("inf")
        for moves in possibleMoves:
            board.add_symbol((moves[0], moves[1]), -1)
            board.isGameOver(point, myTurn)
            newValue, newPoint = minimax(board, depth + 1, alpha, beta, moves, not myTurn)
            check.append((newValue, newPoint))
            if newValue < value:
                value, point = newValue, newPoint
            board.remove_symbol((moves[0], moves[1]))
            # board.setGameOverFalse()
    # print(check)
    print(point, " value: ", value)
    return value, point


def finalHeuristic(board, point, depth):
    dimensions = board.getDimensions()
    score = 0
    target = board.getTarget()

    # if point[0] - target < 0:
    #     xStart = 0
    # else:
    #     xStart = point[0] - target
    # if point[1] - target < 0:
    #     yStart = 0
    # else:
    #     yStart = point[1] - target
    for rowCoord in range(0, dimensions):
        for colCoord in range(0, dimensions):
            score += getScore(board, rowCoord, colCoord, target)
    return score - depth


def getScore(board, x, y, step):
    if board.board[x][y] == 1:
        turn = 1
    else:
        turn = -1
    dimensions = board.getDimensions()
    count_player = 0
    count_opponent = 0
    player = []
    opponent = []
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
        return float("inf")
    elif colCount == -step or rowCount == -step or ndCount == -step or pdCount == -step:
        return float("-inf")
    else:
        return count_player - count_opponent


def heuristic(board_obj, coords):
    target = board_obj.target
    board = board_obj.board
    turn = 0
    # use the coords of the last turn to determine if we are looking for 1 or -1
    if board[coords[0], coords[1]] == 1:
        turn = 1
    elif board[coords[0], coords[1]] == -1:
        turn = -1
    else:
        print("ERROR: Checking for win in unmarked square.")
        exit()

    max_util = 0
    multiplier = 0
    ans = 1
    # check vert, 1
    start_space = [coords[0] - (target - 1), coords[1]]
    for i in range(target):
        if 0 <= start_space[0] <= coords[0]:
            temp = 0
            if (start_space[0] + (target - 1) < len(board)):
                for j in range(target):
                    if board[start_space[0] + j, start_space[1]] == ans:
                        temp += 1
            if (temp == target and ans == turn):
                return float('inf')
            if (ans == turn):
                temp = 0
            if (temp > max_util):
                max_util = temp
                multiplier = 0
            elif (temp == max_util):
                multiplier += 1
        start_space[0] += 1

    # check horiz, 1
    start_space = [coords[0], coords[1] - (target - 1)]
    for i in range(target):
        if start_space[1] >= 0 and start_space[1] <= coords[1]:
            temp = 0
            if (start_space[1] + (target - 1) < len(board)):
                for j in range(target):
                    if board[start_space[0], start_space[1] + j] == ans:
                        temp += 1
            if (temp == target and ans == turn):
                return float('inf')
            if (ans == turn):
                temp -= 1
            if (temp > max_util):
                max_util = temp
                multiplier = 0
            elif (temp == max_util):
                multiplier += 1
        start_space[1] += 1

    # check diag, negative slope, 1
    start_space = [coords[0] - (target - 1), coords[1] - (target - 1)]
    for i in range(target):
        if start_space[0] >= 0 and start_space[0] <= coords[0] and start_space[1] >= 0 and start_space[1] <= coords[
            1]:
            temp = 0
            if (start_space[0] + (target - 1) < len(board) and start_space[1] + (target - 1) < len(board)):
                for j in range(target):
                    if board[start_space[0] + j, start_space[1] + j] == ans:
                        temp += 1
            if (temp == target and ans == turn):
                return float('inf')
            if (ans == turn):
                temp -= 1
            if (temp > max_util):
                max_util = temp
                multiplier = 0
            elif (temp == max_util):
                multiplier += 1
        start_space[0] += 1
        start_space[1] += 1

    # check diag, positive slope, 1
    start_space = [coords[0] + (target - 1), coords[1] - (target - 1)]
    for i in range(target):
        if start_space[0] < len(board) and start_space[0] >= coords[0] and start_space[1] >= 0 and start_space[1] <= \
                coords[1]:
            temp = 0
            if (start_space[0] - (target - 1) >= 0 and start_space[1] + (target - 1) < len(board)):
                for j in range(target):
                    if board[start_space[0] - j, start_space[1] + j] == ans:
                        temp += 1
            if (temp == target and ans == turn):
                return float('inf')
            if (ans == turn):
                temp -= 1
            if (temp > max_util):
                max_util = temp
                multiplier = 0
            elif (temp == max_util):
                multiplier += 1
        start_space[0] -= 1
        start_space[1] += 1

    ans = -1
    # check vert, -1
    start_space = [coords[0] - (target - 1), coords[1]]
    for i in range(target):
        if start_space[0] >= 0 and start_space[0] <= coords[0]:
            temp = 0
            if (start_space[0] + (target - 1) < len(board)):
                for j in range(target):
                    if board[start_space[0] + j, start_space[1]] == ans:
                        temp += 1
            if (temp == target and ans == turn):
                return float('inf')
            if (ans == turn):
                temp -= 1
            if (temp > max_util):
                max_util = temp
                multiplier = 0
            elif (temp == max_util):
                multiplier += 1
        start_space[0] += 1

    # check horiz, -1
    start_space = [coords[0], coords[1] - (target - 1)]
    for i in range(target):
        if start_space[1] >= 0 and start_space[1] <= coords[1]:
            temp = 0
            if (start_space[1] + (target - 1) < len(board)):
                for j in range(target):
                    if board[start_space[0], start_space[1] + j] == ans:
                        temp += 1
            if (temp == target and ans == turn):
                return float('inf')
            if (ans == turn):
                temp -= 1
            if (temp > max_util):
                max_util = temp
                multiplier = 0
            elif (temp == max_util):
                multiplier += 1
        start_space[1] += 1

    # check diag, negative slope, -1
    start_space = [coords[0] - (target - 1), coords[1] - (target - 1)]
    for i in range(target):
        if start_space[0] >= 0 and start_space[0] <= coords[0] and start_space[1] >= 0 and start_space[1] <= coords[
            1]:
            temp = 0
            if (start_space[0] + (target - 1) < len(board) and start_space[1] + (target - 1) < len(board)):
                for j in range(target):
                    if board[start_space[0] + j, start_space[1] + j] == ans:
                        temp += 1
            if (temp == target and ans == turn):
                return float('inf')
            if (ans == turn):
                temp -= 1
            if (temp > max_util):
                max_util = temp
                multiplier = 0
            elif (temp == max_util):
                multiplier += 1
        start_space[0] += 1
        start_space[1] += 1

    # check diag, positive slope, -1
    start_space = [coords[0] + (target - 1), coords[1] - (target - 1)]
    for i in range(target):
        if start_space[0] < len(board) and start_space[0] >= coords[0] and start_space[1] >= 0 and start_space[1] <= \
                coords[1]:
            temp = 0
            if start_space[0] - (target - 1) >= 0 and start_space[1] + (target - 1) < len(board):
                for j in range(target):
                    if board[start_space[0] - j, start_space[1] + j] == ans:
                        temp += 1
            if temp == target and ans == turn:
                return float('inf')
            if ans == turn:
                temp -= 1
            if temp > max_util:
                max_util = temp
                multiplier = 0
            elif temp == max_util:
                multiplier += 1
        start_space[0] -= 1
        start_space[1] += 1

    return max_util + (multiplier / 20)
