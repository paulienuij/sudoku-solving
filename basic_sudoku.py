import numpy as np
from z3 import Int, And, Solver, Distinct

rows = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
COLS = range(9)
ROWS = range(9)

EMPTY_SUDOKU = [[Int(f"{r}{c}") for c in COLS] for r in rows]
# https://ericpony.github.io/z3py-tutorial/guide-examples.htm

class Sudoku:

    def __init__(self):
        x = EMPTY_SUDOKU
        s = Solver()

        # each cell contains a value  in [1, 9]
        s.add([And(1 <= x[r][c], x[r][c] <= 9) for c in range(9) for r in range(9)])

        # each row contains a digit at most once
        s.add([Distinct(x[r]) for r in ROWS])

        # each column contains a digit at most once
        s.add([Distinct([x[r][c] for r in range(9)]) for c in range(9)])

        # each 3x3 square contains a digit at most once
        s.add([Distinct([x[3 * i0 + i][3 * j0 + j]
                          for i in range(3) for j in range(3)])
                            for i0 in range(3) for j0 in range(3)])

        self.s = s
        self.x = x

    def get_cell(self,  row: str, col: int):
        """
        get the cell at given row and column:

            A1 A2 A3 | A4 A5 A6 | A7 A8 A9
            B1 B2 B3 | B4 B5 B6 | B7 B8 B9
            C1 C2 C3 | C4 C5 C6 | C7 C8 C9
            –––––––––+––––––––––+–––––––––
            D1 D2 D3 | D4 D5 D6 | D7 D8 D9
            E1 E2 E3 | E4 E5 E6 | E7 E8 E9
            F1 F2 F3 | F4 F5 F6 | F7 F8 F9
            –––––––––+––––––––––+–––––––––
            G1 G2 G3 | G4 G5 G6 | G7 G8 G9
            H1 H2 H3 | H4 H5 H6 | H7 H8 H9
            I1 I2 I3 | I4 I5 I6 | I7 I8 I9
        """
        if not (1 <= col <= 9):
            raise ValueError("Column should be between 1 and 9")

        r = ord(row) - 65 # convert row letter to index A = 0...
        if not (0 <= r <= 8):
            raise ValueError(f"Row should be in ABC DEF GHI, row={row}")

        return self.x[r][col-1]

    def set_value(self, row: str, col: int, val: int):
        """Set the cell att given row at the given val:  A3 = 4 """
        self.s.add(self.get_cell(row, col) == val)

    def set_row(self, row: str, vals: str):
        """input values for an entire row as a string, using spaces or underscores for unknown cells
        ex:
          - '82  4  6 '
          - "__16__89_"
        """
        for c, val in zip(COLS, vals):
            if val in "123456789":
                self.set_value(row, c+1, int(val))

    def print_solution(self):
        m = self.get_solution()
        for r in ROWS:
            if r % 3 == 0:
                print("+–––––––––+–––––––––+–––––––––+")
            rs = m[r]
            print(f"| {rs[0]}  {rs[1]}  {rs[2]} | {rs[3]}  {rs[4]}  {rs[5]} | {rs[6]}  {rs[7]}  {rs[8]} |")
        print("+–––––––––+–––––––––+–––––––––+")

    def get_solution(self) -> np.array:
        print(self.s.check())
        m = self.s.model()
        return np.array([[m.evaluate(self.x[r][c]).as_long() for c in COLS] for r in ROWS])

