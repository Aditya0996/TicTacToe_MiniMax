import numpy as np

from apis import getBoardStrings, getMoves, getMoveOpponent
from board import Board
from game import startGame
from minimax import minimax, orderHeuristic


def main():
    team2id = 1362
    gameId = 0
    startGame(gameId, team2id)

if __name__ == "__main__":
    main()
