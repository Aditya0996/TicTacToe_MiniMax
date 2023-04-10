import numpy as np


class Board:
    def __init__(self, size, target) -> None:
        self.totalSpaces = size ** 2
        self.dim = size
        self.target = target
        self.middle = size // 2
        self.board = np.zeros((size, size), dtype=np.int8)
        self.current = [self.middle, self.middle]
        self.lastPoint = self.current
        self.gameOver = False

    def get_open_spaces(self):
        return np.argwhere(self.board == 0)

    def isFull(self):
        return True if np.count_nonzero(self.board) == self.totalSpaces else False

    def isEmpty(self):
        return True if np.count_nonzero(self.board) == 0 else False

    def add_symbol(self, point, symbol):
        """point is a int tuple (x,y), symbol 1 or 0"""
        self.lastPoint = self.current
        self.board[point[0]][point[1]] = symbol
        self.current = [point[0], point[1]]

    def remove_symbol(self, point):
        self.board[point[0]][point[1]] = 0

    def getTarget(self):
        return self.target

    def getDimensions(self):
        return self.dim

    def setGameOver(self):
        self.gameOver = True

    def setGameOverFalse(self):
        self.gameOver = False

    def checkWin(self):
        ans = self.gameOver
        self.gameOver = False
        return ans

    def isGameOver(self, point, turn):
        if turn:
            flag = 1
        else:
            flag = -1
        self.checkCol(point[0], point[1], flag)
        self.checkRow(point[0], point[1], flag)
        self.checkDiagonalFromTopLeft(point[0], point[1], flag)
        self.checkDiagonalFromTopRight(point[0], point[1], flag)

    def checkCol(self, x, y, flag):
        i, j = y, y
        while i > -1 and self.board[x][i] == flag:
            i -= 1
        while j < self.dim and self.board[x][j] == flag:
            j += 1
        if j - i - 1 == self.target:
            winner = self.board[x][y]
            self.gameOver = True

    def checkRow(self, x, y, flag):
        i, j = x, x
        while i > -1 and self.board[i][y] == flag:
            i -= 1
        while j < self.dim and self.board[j][y] == flag:
            j += 1
        if j - i - 1 == self.target:
            winner = self.board[x][y]
            self.gameOver = True

    def checkDiagonalFromTopLeft(self, x, y, flag):
        ix, jx, iy, jy = x, x, y, y
        while ix > -1 and iy < self.dim and self.board[ix][iy] == flag:
            ix -= 1
            iy += 1
        while jy > -1 and jx < self.dim and self.board[jx][jy] == flag:
            jx += 1
            jy -= 1
        if jx - ix - 1 == self.target:
            winner = self.board[x][y]
            self.gameOver = True

    def checkDiagonalFromTopRight(self, x, y, flag):
        ix, jx, iy, jy = x, x, y, y
        while ix > -1 and iy > -1 and self.board[ix][iy] == flag:
            ix -= 1
            iy -= 1
        while jx < self.dim and jy < self.dim and self.board[jx][jy] == flag:
            jx += 1
            jy += 1
        if jx - ix - 1 == self.target:
            winner = self.board[x][y]
            self.gameOver = True
