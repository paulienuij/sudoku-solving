# A1 A2 A3 | A4 A5 A6 | A7 A8 A9
# B1 B2 B3 | B4 B5 B6 | B7 B8 B9
# C1 C2 C3 | C4 C5 C6 | C7 C8 C9
# –––––––––+––––––––––+–––––––––
# D1 D2 D3 | D4 D5 D6 | D7 D8 D9
# E1 E2 E3 | E4 E5 E6 | E7 E8 E9
# F1 F2 F3 | F4 F5 F6 | F7 F8 F9
# –––––––––+––––––––––+–––––––––
# G1 G2 G3 | G4 G5 G6 | G7 G8 G9
# H1 H2 H3 | H4 H5 H6 | H7 H8 H9
# I1 I2 I3 | I4 I5 I6 | I7 I8 I9

from z3 import Int, And, Solver, Distinct

rows = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
COLS = range(9)
ROWS = range(9)

EMPTY_SUDOKU = [[Int(f"{r}{c}") for c in COLS] for r in rows]


# https://ericpony.github.io/z3py-tutorial/guide-examples.htm


class BaseSudoku:

    def __init__(self):
        x = EMPTY_SUDOKU
        s = Solver()

        # each cell contains a value  in [1, 9]
        limit_1_to_9 = [And(1 <= x[r][c], x[r][c] <= 9) for c in range(9) for r in range(9)]
        s.add(limit_1_to_9)

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

    def set_value(self, row, col, val):
        r = ord(row-65) # convert row letter to index A = 0...
        self.s.add(self.x[r][col] == val)

    def print_solution(self):
        self.s.check()
        m = self.s.model()
        for r in ROWS:
            if r % 3 == 0:
                print("+–––––––––+–––––––––+–––––––––+")

            rs = [str(m.evaluate(self.x[r][c])) for c in COLS]
            print(f"| {rs[0]}  {rs[1]}  {rs[2]} | {rs[3]}  {rs[4]}  {rs[5]} | {rs[6]}  {rs[7]}  {rs[8]} |")
        print("+–––––––––+–––––––––+–––––––––+")


if __name__ == "__main__":
    sudoku = BaseSudoku()
    sudoku.print_solution()
