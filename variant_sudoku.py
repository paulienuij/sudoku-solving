from z3 import Sum, Distinct, Or, If, And

from basic_sudoku import Sudoku


class SudokuVariant(Sudoku):

    def __init__(self):
        super().__init__()
        self.german_whisper_hints = []
        self.x_hints = []

    def add_killerbox_with_repeats(self, value: int, cells: list):
        cells = [self.get_cell(c[0], int(c[1])) for c in cells]
        self.s.add(Sum(cells) == value)

    def add_killerbox(self, value: int, cells: list):
        cells = [self.get_cell(c[0], int(c[1])) for c in cells]
        self.s.add(Sum(cells) == value)
        self.s.add(Distinct(cells))

    def add_german_whisper(self, cells: list):
        self.german_whisper_hints.append(cells)
        cells = [self.get_cell(c[0], int(c[1])) for c in cells]
        for c1, c2 in zip(cells[:-1], cells[1:]):
            diff_more_than_5 = If(c1 > c2, c1 - c2 > 4, c2 - c1 > 4)
            self.s.add(diff_more_than_5)

    def add_x(self, cells):
        self.x_hints.append(cells)
        cells = [self.get_cell(c[0], int(c[1])) for c in cells]
        c1 = cells[0]
        c2 = cells[1]

        # list all states where c1, c2 do add to 10 and add condition 1 of them is true
        sum_to_10 = [[1, 9], [2, 8], [3, 7], [4, 6]]
        valid_states = []
        for x1, x2 in sum_to_10:
            # (c1=1 and c2=9) OR (c1=9 and c2=1)
            valid_states.append(And(c1 == x1, c2 == x2))
            valid_states.append(And(c1 == x2, c2 == x1))

        # all options are mutually exclusive, one of them holds
        self.s.add(Or(valid_states))
