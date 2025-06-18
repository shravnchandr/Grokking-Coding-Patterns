from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        EMPTY, FRESH, ROTTEN = 0, 1, 2
        row_count, column_count = len(grid), len(grid[0])

        rotten_cells, rotten_queue = set(), deque()
        for row_index in range(row_count):
            for column_index in range(column_count):
                
                if grid[row_index][column_index] == ROTTEN:
                    rotten_cells.add((row_index, column_index))
                    rotten_queue.append((row_index, column_index))

        directions = ((0,1), (1,0), (0,-1), (-1,0))

        def breadthFirstSearch(old_queue: deque) -> deque:
            new_queue = deque()

            while old_queue:
                row_index, column_index = old_queue.popleft()

                for row_dir,column_dir in directions:
                    next_row, next_column = row_index + row_dir, column_index + column_dir
                    if 0 <= next_row < row_count and 0 <= next_column < column_count and (next_row,next_column) not in rotten_cells:
                        
                        if grid[next_row][next_column] == FRESH:
                            grid[next_row][next_column] = ROTTEN
                            rotten_cells.add((next_row, next_column))
                            new_queue.append((next_row, next_column))

            return new_queue


        total_time = 0
        while rotten_queue:
            rotten_queue = breadthFirstSearch(rotten_queue)
            if rotten_queue:
                total_time = total_time +1

        for row_index in range(row_count):
            for column_index in range(column_count):
                
                if grid[row_index][column_index] == FRESH:
                    return -1
                
        return total_time


        