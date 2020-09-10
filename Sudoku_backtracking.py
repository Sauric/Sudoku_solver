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

# def solve(sudoku):
#
#     find = find_(sudoku)
#     if not find:
#         return True
#
#     for i in [str(i) for i in range(1,10)]:
#         if valid_(sudoku, i, find):
#             sudoku[find[0]][find[1]] = i
#             if solve(sudoku):
#                 return True
#
#             sudoku[find[0]][find[1]] = "."
#     return False
#
#
# def solveSudoku(board):
#     squares = [
#         [(2, 2), (2, 5), (2, 8)],
#         [(5, 2), (5, 5), (5, 8)],
#         [(8, 2), (8, 5), (8, 8)]
#     ]
#
#     def possible(row, col):  # returns possible numbers
#         possib = {str(i) for i in range(1, 10)}
#         for i in range(9):
#             elem_col = board[i][col]
#             elem_row = board[row][i]
#             if elem_col in possib:
#                 possib.remove(elem_col)
#             if elem_row in possib:
#                 possib.remove(elem_row)
#         sq = squares[row // 3][col // 3]
#         for r in range(sq[0] - 2, sq[0] + 1):
#             for c in range(sq[1] - 2, sq[1] + 1):
#                 elem = board[r][c]
#                 if elem in possib:
#                     possib.remove(elem)
#         return possib
#
#     cycle = 0
#     while cycle < 200:
#         for row in range(9):
#             for col in range(9):
#                 cycle += 1
#                 if board[row][col] == ".":
#                     pos = possible(row, col)
#                     if len(pos) == 1:
#                         board[row][col] = pos.pop()
#
#     return True

# def main():
#     sudoku = [
#         ["5", "3", ".", ".", "7", ".", ".", ".", "."],
#         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
#         [".", "9", "8", ".", ".", ".", ".", "6", "."],
#         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
#         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
#         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
#         [".", "6", ".", ".", ".", ".", "2", "8", "."],
#         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
#         [".", ".", ".", ".", "8", ".", ".", "7", "9"]
#     ]
#     sudoku = [
#               [".",".","9","7","4","8",".",".","."],
#               ["7",".",".",".",".",".",".",".","."],
#               [".","2",".","1",".","9",".",".","."],
#               [".",".","7",".",".",".","2","4","."],
#               [".","6","4",".","1",".","5","9","."],
#               [".","9","8",".",".",".","3",".","."],
#               [".",".",".","8",".","3",".","2","."],
#               [".",".",".",".",".",".",".",".","6"],
#               [".",".",".","2","7","5","9",".","."]
#     ]
#     print_(sudoku)
#     # solve(sudoku)
#     solveSudoku(sudoku)
#     print('_______________________________')
#     print_(sudoku)
#     # solve(sudoku)
#     # print('_______________________________')
#     # print_(sudoku)
#
#
# if __name__ == '__main__':
#     main()
