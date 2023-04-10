import numpy as np

from apis import getBoardStrings, getMoves
from board import Board
from game import startGame
from minimax import minimax


def main():
    team2id = 1362
    gameId = 0
    # startGame(gameId, team2id)
    # print(getMoves(gameId, 1))
    # boardString = getBoardStrings(gameId)
    # board = Board(boardString["size"], boardString["target"])
    # board.add_symbol((0, 1), 1)
    # print(board.get_open_spaces())
    size = 5
    # board = Board(5, 4)
    # board.board[1][1] = -1
    # board.board[2][1] = 1
    # board.board[1][3] = -1
    # board.board[2][3] = -1
    # board.board[2][2] = 1
    # board.board[3][3] = 1
    # board.board[1][0] = 1
    # board.board[1][2] = -1
    board = Board(3, 3)
    board.board[0][0] = -1
    board.board[2][0] = -1
    board.board[1][1] = 1
    print(board.board)
    print(minimax(board, 0, 0, 0))



if __name__ == "__main__":
    main()
