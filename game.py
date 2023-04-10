import time

from apis import getBoardStrings, makeMove, createGame, getMoves
from board import Board
from constants import dimensions, target
from minimax import minimax


def startGame(gameId, team2Id):
    flag = True
    if gameId == 0:
        gameId = createGame(team2Id, dimensions, target)
        print(gameId)
    boardString = getBoardStrings(gameId)
    board = Board(boardString["size"], boardString["target"])
    # Update with first move
    while flag:
        moveMade, point = game(gameId, board)
        if moveMade["code"] == "FAIL":
            if "Game is no longer open" in moveMade["message"]:
                print("Game Over")
                flag = False
            else:
                time.sleep(2)
        else:
            board.add_symbol((point[0], point[1]), 1)
            moveId = moveMade["moveId"]
            while moveId == getMoves(gameId, 1)["moveId"]:
                time.sleep(2)
            lastMove = getMoves(gameId, 1)
            x, y = lastMove["x"], lastMove["y"]
            board.add_symbol((x, y), -1)


def game(gameId, board):
    value, points = minimax(board, 0, 0, 0, None, True)
    moveCoordinates = formatCoordinates(points)
    return makeMove(gameId, moveCoordinates), points


def formatCoordinates(points):
    return str(points[0]) + "," + str(points[1])
