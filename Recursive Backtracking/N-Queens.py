from typing import List
import numpy


class Solution:
    def solveNQueens(self, board_size: int) -> List[List[str]]:

        def check_row(row_index: int, column_index: int) -> bool:
            