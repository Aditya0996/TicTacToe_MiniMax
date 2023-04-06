import time

from apis import getBoardStrings, makeMove, getMoves, createGame
from randomMove import random


def game(gameId):
    board = getBoardStrings(gameId)
    print(board)
    move = random(board)
    return makeMove(gameId, move)


def main():
    flag = True
    team2id = 1362
    gameId = 0
    if gameId == 0:
        gameId = createGame(team2id,6,4)
        print(gameId)
    while flag:
        moveMade = game(gameId)
        if moveMade["code"] == "FAIL":
            if "Game is no longer open" in moveMade["message"]:
                print("Game Over")
                flag = False
            else:
                time.sleep(2)
        else:
            moveId = moveMade["moveId"]
            while moveId == getMoves(gameId, 1):
                time.sleep(2)


if __name__ == "__main__":
    main()
