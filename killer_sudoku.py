from z3 import Sum

from basic_sudoku import Sudoku


class KillerSudoku(Sudoku):

    def __init__(self):
        super().__init__()

    def add_killerbox(self, value: int, cells: list):
        cells = [self.get_cell(c[0], int(c[1])) for c in cells]
        self.s.add(Sum(cells) == value)


