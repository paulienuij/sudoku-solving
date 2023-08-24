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

    plt.show()
