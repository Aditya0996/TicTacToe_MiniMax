import time

import numpy as np

import constants
from apis import getBoardStrings, getMoves, getMoveOpponent
from board import Board
from game import startGame
from minimax import minimax, orderHeuristic


def main():
    # start_time = time.time()
    team2id = 1362
    gameId = 0
    startGame(gameId, team2id)
    # board = Board(12, 5)
    # board.board = np.array     ([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    #                            , [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    #                            , [0, 0, 0, 0,-1, 0,-1, 0, 0, 0, 0, 0]
    #                            , [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
    #                            , [0, 0, 0,-1, 1, 0, 1, 0, 0, 0, 0, 0]
    #                            , [0,-1, 1, 1, 1, 1,-1, 1, 0, 0, 0, 0]
    #                            , [0, 0, 1, 0,-1, 0,-1, 0, 0, 0, 0, 0]
    #                            , [0, 1, 0, 0, 0,-1,-1, 0, 0, 0, 0, 0]
    #                            , [0, 0, 0, 0,-1, 0,-1, 0, 0, 0, 0, 0]
    #                            , [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
    #                            , [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    #                            , [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
    # print(board.board)
    # print(minimax(board, 0, []))
    # board.showBoard()
    # board.finalShow()
    # board = Board(3, 3)
    # board.board[1][1] = -1
    # board.board[0][0] = 1
    # board.board[2][2] = -1
    # print(board.board)
    # print(minimax(board, 0, []))

    # print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    main()
