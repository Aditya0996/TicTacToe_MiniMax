import time

from apis import getBoardStrings, makeMove, getMoves
from randomMove import random


def game(gameId):
    board = getBoardStrings(gameId)
    print(board)
    move = random(board)
    return makeMove(gameId, move)


def main():
    flag = True
    gameId = "3765"
    while flag:
        moveMade = game(gameId)
        if moveMade["code"] == "FAIL":
            if "Game is no longer open" in moveMade["message"]:
                print("Game Over")
                flag = False
        else:
            moveId = moveMade["moveId"]
            while moveId == getMoves(gameId, 1):
                time.sleep(2)


if __name__ == "__main__":
    main()
