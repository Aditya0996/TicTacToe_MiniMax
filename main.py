import time

import numpy as np

from apis import getBoardStrings, getMoves, getMoveOpponent
from board import Board
from game import startGame
from minimax import minimax, orderHeuristic


def main():
    start_time = time.time()
    team2id = 1362
    gameId = 4033
    startGame(gameId, team2id)
#     print("--- %s seconds ---" % (time.time() - start_time))
if __name__ == "__main__":
    main()
