import time


class sudoku():
    def __init__(self, temp=False):
        board = [
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"]
        ]
        if not temp:
            self.board = [["" for i in range(9)] for j in range(9)]
            for i in range(9):
                for j in range(9):
                    self.board[i][j] = [board[i][j], True] if board[i][j] in "123456789" else [board[i][j], False]
            self.full = "full"
        else:
            self.board = [[["", False] for i in range(9)] for j in range(9)]
            self.full = "empty"

    def insert(self, num):
        for i in range(9):
            for j in range(9):
                if self.board[i][j][0] == "":
                    if num in '123456789':
                        self.board[i][j] = [num, True]
                    else:
                        self.board[i][j][0] = "."
                    return None
        self.full = "full"
        print(self.full)
        return True

    def print_(self):
        print("_________________________")
        for i in range(9):
            if i % 3 == 0 and i != 0:
                print('- - - - - - - - - - - -')

            for j in range(9):
                if j % 3 == 0 and j != 0:
                    print(' | ', end='')

                if j == 8:
                    print(self.board[i][j][0])
                else:
                    print(self.board[i][j][0], end=' ')
        return None

    def copy_(self):
        return [[i for i in self.board[j]] for j in range(9)]

    def clear(self):
        for i in range(9):
            for j in range(9):
                self.board[i][j][0], self.board[i][j][1] = "", False

        self.full = "empty"
        return None

    def del_last(self):

        for i in range(8, -1, -1):
            for j in range(8, -1, -1):
                if self.board[i][j][0] != "":
                    self.board[i][j][0], self.board[i][j][1] = "", False
                    return None


def find_(su):
    for i in range(9):
        for j in range(9):
            if su[i][j][0] == ".":
                return (i, j)


def valid_(su, num, ind):
    # num = su[ind[0]][ind[1]]
    for i in range(9):
        # check row
        if i != ind[1] and su[ind[0]][i][0] == num:
            # print('row')
            return False
        # check col
        if i != ind[0] and su[i][ind[1]][0] == num:
            # print('col')
            return False

    # check box
    box = (ind[0] // 3, ind[1] // 3)
    for i in range(box[0] * 3, box[0] * 3 + 3):
        for j in range(box[1] * 3, box[1] * 3 + 3):
            # print(su[i][j])
            if (i != ind[0] or j != ind[1]) and su[i][j][0] == num:
                # print(('box'))
                return False
    return True


