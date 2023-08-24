import unittest

import numpy as np

from basic import simple_hint, simple_ans, hard_hint, hard_ans
from basic_sudoku import Sudoku
from killer import killer_hint, killer_cell_hints, killer_ans, crypic_hint
from variant_sudoku import SudokuVariant


class TestingBasicSudokuSolver(unittest.TestCase):

    def test_basic_sudoku_solver_easy(self):
        base_sudoku = Sudoku()
        for row, row_hint in zip("ABCDEFGHI", simple_hint):
            base_sudoku.set_row(row, row_hint)

        result = base_sudoku.get_solution()
        ans = np.array(simple_ans)
        assert np.all(result == ans)

    def test_basic_sudoku_solver_hard(self):
        base_sudoku = Sudoku()
        for row, row_hint in zip("ABCDEFGHI", hard_hint):
            base_sudoku.set_row(row, row_hint)

        ans = np.array(hard_ans)
        result = base_sudoku.get_solution()
        assert np.all(result == ans)

    def test_killer_solver_easy(self):
        sudoku = SudokuVariant()
        for row, row_hint in zip("ABCDEFGHI", killer_hint):
            sudoku.set_row(row, row_hint)

        for s, cells in killer_cell_hints:
            cell_names = cells.split(",")
            sudoku.add_killerbox_with_repeats(s, cell_names)

        ans = np.array(killer_ans)
        result = sudoku.get_solution()
        assert np.all(result == ans)


if __name__ == '__main__':
    unittest.main()
