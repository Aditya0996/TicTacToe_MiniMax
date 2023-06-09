import numpy as np
from matplotlib import pyplot


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
        self.fig, self.ax = pyplot.subplots()
        self.table = self.ax.table(cellText=self.board, cellLoc='center', cellColours=np.full((size, size), 'white'),
                         loc='center')
        self.ax.axis('off')

    def showBoard(self):
        cell_text = {1: 'O', -1: 'X', 0: ''}
        cell_colors = {1: 'tab:red', -1: 'tab:blue', 0: 'white'}
        board_str = [[cell_text[cell] for cell in row] for row in self.board]
        board_colors = [[cell_colors[cell] for cell in row] for row in self.board]
        self.ax.table(cellText=board_str, cellLoc='center', cellColours=board_colors, loc='center')
        pyplot.draw()
        pyplot.show(block=False)
        pyplot.pause(1)

    def finalShow(self):
        cell_text = {1: 'X', -1: 'O', 0: ''}
        cell_colors = {1: 'tab:red', -1: 'tab:blue', 0: 'white'}
        board_str = [[cell_text[cell] for cell in row] for row in self.board]
        board_colors = [[cell_colors[cell] for cell in row] for row in self.board]
        self.ax.table(cellText=board_str, cellLoc='center', cellColours=board_colors, loc='center')
        self.ax.axis('off')
        pyplot.show()

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
        self.checkDiagonalPositive(point[0], point[1], flag)
        self.checkDiagonalNegative(point[0], point[1], flag)

    def checkRow(self, x, y, flag):
        i, j = y, y
        while i > -1 and self.board[x][i] == flag:
            i -= 1
        while j < self.dim and self.board[x][j] == flag:
            j += 1
        if j - i - 1 == self.target:
            self.gameOver = True

    def checkCol(self, x, y, flag):
        i, j = x, x
        while i > -1 and self.board[i][y] == flag:
            i -= 1
        while j < self.dim and self.board[j][y] == flag:
            j += 1
        if j - i - 1 == self.target:
            self.gameOver = True

    def checkDiagonalPositive(self, x, y, flag):
        ix, jx, iy, jy = x, x, y, y
        while ix > -1 and iy < self.dim and self.board[ix][iy] == flag:
            ix -= 1
            iy += 1
        while jy > -1 and jx < self.dim and self.board[jx][jy] == flag:
            jx += 1
            jy -= 1
        if jx - ix - 1 == self.target:
            self.gameOver = True

    def checkDiagonalNegative(self, x, y, flag):
        ix, jx, iy, jy = x, x, y, y
        while ix > -1 and iy > -1 and self.board[ix][iy] == flag:
            ix -= 1
            iy -= 1
        while jx < self.dim and jy < self.dim and self.board[jx][jy] == flag:
            jx += 1
            jy += 1
        if jx - ix - 1 == self.target:
            self.gameOver = True
