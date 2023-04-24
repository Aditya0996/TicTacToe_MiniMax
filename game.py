import time

import constants
from apis import getBoardStrings, makeMove, createGame, getMoves, getMoveOpponent
from board import Board
from constants import dimensions, target
from minimax import minimax


def startGame(gameId, team2Id, firstMove=False):
    print("Started Game")
    flag = True
    if gameId == 0:
        gameId = createGame(team2Id, dimensions, target)
        firstMove = True
        print(gameId)
        time.sleep(2)
    boardString = getBoardStrings(gameId)
    board = Board(boardString["size"], boardString["target"])
    if firstMove:
        startx = starty = board.middle
        moved = makeMove(gameId, str(startx) + "," + str(starty))
        if moved["code"] == "OK":
            firstMove = False
            board.add_symbol((startx, starty), 1)
            print(board.board)
            board.showBoard()
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
            board.showBoard()
    else:
        while getMoveOpponent(gameId, 1) == "FAIL":
            time.sleep(2)
        lastMove = getMoves(gameId, 1)
        x, y = lastMove["x"], lastMove["y"]
        board.add_symbol((x, y), -1)
        print(board.board)
        board.showBoard()
    while flag:
        moveMade, point = game(gameId, board)
        time.sleep(2)
        if moveMade["code"] == "FAIL":
            time.sleep(2)
        else:
            board.add_symbol([point[0], point[1]], 1)
            board.isGameOver(point, 1)
            print("our move:")
            print(board.board)
            board.showBoard()
            lastMove = getMoves(gameId, 1)
            moveX, moveY = lastMove["x"], lastMove["y"]
            while moveX == point[0] and moveY == point[1]:
                time.sleep(3)
                lastMove = getMoves(gameId, 1)
                moveX, moveY = lastMove["x"], lastMove["y"]
            x, y = lastMove["x"], lastMove["y"]
            board.add_symbol((x, y), -1)
            print("opponent move:")
            print(board.board)
            board.showBoard()


def game(gameId, board):
    print("Starting minimax")
    openSpaces = len(board.get_open_spaces())
    if openSpaces > 30:
        constants.maxDepth = 2
    elif openSpaces > 20:
        constants.maxDepth = 3
    elif openSpaces > 10:
        constants.maxDepth = 4
    else:
        constants.maxDepth = 10
    value, points = minimax(board, 0, [])
    print(points)
    moveCoordinates = formatCoordinates(points)
    return makeMove(gameId, moveCoordinates), points


def formatCoordinates(points):
    return str(points[0]) + "," + str(points[1])
