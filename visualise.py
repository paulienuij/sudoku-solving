import matplotlib.pyplot as plt

from basic_sudoku import Sudoku
from variant_sudoku import SudokuVariant


def plot_sudoku(sudoku: SudokuVariant):
    """plot to see if hints have been entered correctly"""
    fig, ax = plt.subplots()

    for whisper in sudoku.german_whisper_hints:
        rows = [-(ord(cell[0]) - 65)for cell in whisper]
        cols = [int(cell[1]) for cell in whisper]
        ax.plot(cols, rows)

    for whisper in sudoku.x_hints:
        row = sum([-(ord(cell[0]) - 65)for cell in whisper])/2
        col = sum([int(cell[1]) for cell in whisper])/2
        ax.text(col, row, "X")

    plt.xlim([0, 10])
    plt.ylim([0, -10])
    plt.show()
