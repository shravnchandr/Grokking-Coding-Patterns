from collections import deque
from typing import List


class Solution:
    def wallsAndGates(self, rooms_grid: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        
        row_count, column_count = len(rooms_grid), len(rooms_grid[0])

        WALL, GATE, EMPTY = -1, 0, 2**31 -1
        directions = ((0,1), (1,0), (0,-1), (-1,0))

        gate_cells = deque()
        for row_index in range(row_count):
            for column_index in range(column_count):

                if rooms_grid[row_index][column_index] == GATE:
                    gate_cells.append((row_index, column_index))

        while gate_cells:
            row_index, column_index = gate_cells.popleft()

            for next_row, next_column in directions:
                new_row, new_column = row_index + next_row, column_index + next_column

                if 0 <= new_row < row_count and 0 <= new_column < column_count and rooms_grid[new_row][new_column] == EMPTY:
                    rooms_grid[new_row][new_column] = rooms_grid[row_index][column_index] +1
                    gate_cells.append((new_row, new_column))

        