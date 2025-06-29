from typing import List


class Solution:
    def solveNQueens(self, board_size: int) -> List[List[str]]:
        solutions_list = list()

        occupied_columns = set()
        occupied_left_diagonals, occupied_right_diagonals = set(), set()
        
        def queen_ok(row_index: int, column_index: int) -> bool:
            row_ok = True
            column_ok = column_index not in occupied_columns
            left_diagonal_ok = (row_index - column_index) not in occupied_left_diagonals
            right_diagonal_ok = (row_index + column_index) not in occupied_right_diagonals

            return row_ok and column_ok and left_diagonal_ok and right_diagonal_ok

        def recursive_backtracking(row_index: int, current_board: List[str]) -> None:
            if row_index == board_size:
                solutions_list.append(current_board[:])
                return

            for column_index in range(board_size):

                if queen_ok(row_index, column_index):
                    occupied_columns.add(column_index)
                    occupied_left_diagonals.add(row_index - column_index)
                    occupied_right_diagonals.add(row_index + column_index)

                    current_row = '.' * column_index + 'Q' + '.' * (board_size - column_index -1)

                    current_board.append(current_row)
                    recursive_backtracking(row_index +1, current_board)
                    current_board.pop()

                    occupied_columns.remove(column_index)
                    occupied_left_diagonals.remove(row_index - column_index)
                    occupied_right_diagonals.remove(row_index + column_index)

        recursive_backtracking(0, list())
        return solutions_list
