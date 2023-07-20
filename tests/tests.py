import unittest

import numpy as np

from basic_sudoku import Sudoku
from hard import hard_hint, hard_ans
from simple import simple_hint, simple_ans


class TestingBasicSudokuSolver(unittest.TestCase):

    def test_basic_sudoku_solver_easy(self):
        base_sudoku = Sudoku()
        for row, row_hint in zip("ABCDEFGHI", simple_hint):
            base_sudoku.set_row(row, row_hint)

        result = base_sudoku.get_solution()
        ans = np.array(simple_ans)
        assert np.alltrue(result == ans)

    def test_basic_sudoku_solver_hard(self):
        base_sudoku = Sudoku()
        for row, row_hint in zip("ABCDEFGHI", hard_hint):
            base_sudoku.set_row(row, row_hint)

        ans = np.array(hard_ans)
        result = base_sudoku.get_solution()
        assert np.alltrue(result == ans)


if __name__ == '__main__':
    unittest.main()
