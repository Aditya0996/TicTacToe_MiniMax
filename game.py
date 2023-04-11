import time

from apis import getBoardStrings, makeMove, createGame, getMoves, getMoveOpponent
from board import Board
from constants import dimensions, target
from minimax import minimax


def startGame(gameId, team2Id, firstMove=True):
    print("Started Game")
    flag = True
    if gameId == 0:
        gameId = createGame(team2Id, dimensions, target)
        print(gameId)
        time.sleep(5)
        opponentStarts = False
    else:
        opponentStarts = True
    boardString = getBoardStrings(gameId)
    board = Board(boardString["size"], boardString["target"])
    if firstMove:
        startx = starty = board.middle
        if opponentStarts:
            while getMoveOpponent(gameId, 1) == "FAIL":
                time.sleep(1)
                print("Maybe game over buddy")
                print(board.board)
            time.sleep(1)
            lastMove = getMoves(gameId, 1)
            x, y = lastMove["x"], lastMove["y"]
            board.add_symbol((x, y), -1)
            if x == startx and y == starty:
                starty += 1
        while firstMove:
            moved = makeMove(gameId, str(startx)+","+str(starty))
            if moved["code"] == "OK":
                firstMove = False
                board.add_symbol((startx, starty), 1)
                print(board.board)
    while flag:
        time.sleep(2)
        lastMove = getMoves(gameId, 1)
        moveX, moveY = lastMove["x"], lastMove["y"]
        while moveX == startx and moveY == starty:
            time.sleep(2)
            lastMove = getMoves(gameId, 1)
            moveX, moveY = lastMove["x"], lastMove["y"]
        x, y = lastMove["x"], lastMove["y"]
        board.add_symbol((x, y), -1)
        print(board.board)
        moveMade, point = game(gameId, board)
        time.sleep(2)
        if moveMade["code"] == "FAIL":
            time.sleep(2)
        else:
            board.add_symbol([point[0], point[1]], 1)
            board.isGameOver(point, 1)
            print("our move:")
            print(board.board)
            lastMove = getMoves(gameId, 1)
            moveX, moveY = lastMove["x"], lastMove["y"]
            while moveX == point[0] and moveY == point[1]:
                time.sleep(2)
                lastMove = getMoves(gameId, 1)
                moveX, moveY = lastMove["x"], lastMove["y"]
            x, y = lastMove["x"], lastMove["y"]
            board.add_symbol((x, y), -1)
            print("opponent move:")
            print(board.board)


def game(gameId, board):
    print("Starting minimax")
    value, points = minimax(board, 0, [])
    print(points)
    moveCoordinates = formatCoordinates(points)
    return makeMove(gameId, moveCoordinates), points


def formatCoordinates(points):
    return str(points[0]) + "," + str(points[1])
