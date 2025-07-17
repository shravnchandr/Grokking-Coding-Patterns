from collections import deque
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        row_count, column_count = len(board), len(board[0])
        directions = ((0,1), (1,0), (0,-1), (-1,0))

        regions_queue = deque()
        for row_index in range(row_count):
            for column_index in range(column_count):

                 if row_index in [0, row_count -1] or column_index in [0, column_count -1]:
                      if board[row_index][column_index] == 'O':
                        regions_queue.append((row_index, column_index))     

        while regions_queue:
            row_index, column_index = regions_queue.popleft()
            board[row_index][column_index] = 'Z'

            for row_dir, column_dir in directions:
                next_row, next_column = row_index + row_dir, column_index + column_dir

                if 0 <= next_row < row_count and 0 <= next_column < column_count and board[next_row][next_column] == 'O':
                    regions_queue.append((next_row, next_column))

        for row_index in range(row_count):
            for column_index in range(column_count):

                board[row_index][column_index] = 'O' if board[row_index][column_index] == 'Z' else 'X'


