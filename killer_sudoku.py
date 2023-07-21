from z3 import Sum, Distinct

from basic_sudoku import Sudoku


class KillerSudoku(Sudoku):

    def __init__(self):
        super().__init__()

    def add_killerbox(self, value: int, cells: list):
        cells = [self.get_cell(c[0], int(c[1])) for c in cells]
        self.s.add(Sum(cells) == value)

    def add_killerbox_no_repeats(self, value: int, cells: list):
        cells = [self.get_cell(c[0], int(c[1])) for c in cells]
        self.s.add(Sum(cells) == value)
        self.s.add(Distinct(cells))


if __name__ == '__main__':
    # https://app.crackingthecryptic.com/sudoku/mJqT6RDG2L
    # this one has no normal hints only cages
    crypic_hint = [
        (37, "B1,B2,C1,C2,D1,D2,D3,E1"),
        (13, "C6,D6,D7,E7"),
        (7, "B7,C7,C8"),
        (24, "E9,F9,G9"),
        (37, "F3,F4,G2,G3,G4,H3"),
        (16, "I5,I6,H6,H7,I7")
    ]

    sudoku = KillerSudoku()

    for s, cells in crypic_hint:
        cell_names = cells.split(",")
        sudoku.add_killerbox_no_repeats(s, cell_names)

    sudoku.print_solution()
