"""
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
from variant_sudoku import SudokuVariant

# LAYLA
# this one has no normal hints only cages
# https://logic-masters.de/Raetselportal/Raetsel/zeigen.php?id=000BI4
lyla_hint = [
    (37, "B1,B2,C1,C2,D1,D2,D3,E1"),
    (13, "C6,D6,D7,E7"),
    (7, "B7,C7,C8"),
    (24, "E9,F9,G9"),
    (37, "F3,F4,G2,G3,G4,H3"),
    (16, "I5,I6,H6,H7,I7")
]

# HUMMING AND SUMMING
# https://logic-masters.de/Raetselportal/Raetsel/zeigen.php?id=000EE7
# https://tinyurl.com/5yzvk34w
summing_hints = [
    (9, "A1,B1,C1"),
    (13, "C2,C3"),
    (9, "B4,B5,B6"),
    (21, "A7,A8,A9"),
    (12, "B9,C9"),
    (21, "D2,E2,F2"),
    (21, "D8,E8,F8"),
    (10, "G3,H3,I3"),
    (22, "H4,H5,H6"),
    (11, "G7,H7,I7"),
    (13, "G8,G9")
]
humming_hint = [
    "C6,D7",
    "E4,F3,G4,F5,G6,F7"
]


if __name__ == '__main__':

    # INPUT HERE
    killer_hint = summing_hints
    whisper_hint = humming_hint

    sudoku = SudokuVariant()
    for s, cells in killer_hint:
        cell_names = cells.split(",")
        sudoku.add_killerbox(s, cell_names)

    for cells in whisper_hint:
        cell_names = cells.split(",")
        sudoku.add_german_whisper(cell_names)

    sudoku.print_solution()
