from z3 import Sum, Distinct, Or, If

from basic_sudoku import Sudoku


class SudokuVariant(Sudoku):

    def __init__(self):
        super().__init__()

    def add_killerbox_with_repeats(self, value: int, cells: list):
        cells = [self.get_cell(c[0], int(c[1])) for c in cells]
        self.s.add(Sum(cells) == value)

    def add_killerbox(self, value: int, cells: list):
        cells = [self.get_cell(c[0], int(c[1])) for c in cells]
        self.s.add(Sum(cells) == value)
        self.s.add(Distinct(cells))

    def add_german_whisper(self, cells: list):
        cells = [self.get_cell(c[0], int(c[1])) for c in cells]
        for c1, c2 in zip(cells[:-1], cells[1:]):
            diff_more_than_5 = If(c1 > c2, c1 - c2 > 4, c2 - c1 > 4)
            self.s.add(diff_more_than_5)


