from typing import List


class Solution:
    def minPathSum(self, numbers_grid: List[List[int]]) -> int:
        row_count, column_count = len(numbers_grid), len(numbers_grid[0])

        directions = ((0,1), (1,0), (0,-1), (-1,0))
        visited_cells = set()

        dp_memoization = {}
        def depth_first_search(row_index: int, column_index: int) -> int:
            if row_index == row_count -1 and column_index == column_count -1:
                return numbers_grid[row_index][column_index]
            
            if (row_index, column_index) in dp_memoization:
                return dp_memoization[(row_index, column_index)]

            # visited_cells.add((row_index, column_index))
            min_path = float('inf')

            for row_dir, column_dir in directions:
                next_row, next_column = row_index + row_dir, column_index + column_dir

                if 0 <= next_row < row_count and 0 <= next_column < column_count and \
                    (next_row, next_column) not in visited_cells:
                    
                    visited_cells.add((next_row, next_column))
                    min_path = min(min_path, depth_first_search(next_row, next_column))
                    visited_cells.remove((next_row, next_column))

            # visited_cells.remove((row_index, column_index))

            dp_memoization[(row_index, column_index)] = min_path + numbers_grid[row_index][column_index]
            return dp_memoization[(row_index, column_index)]
        
        visited_cells.add((0,0))
        return depth_first_search(0, 0)

    
    def minPathSum(self, numbers_grid: List[List[int]]) -> int:
        row_count, column_count = len(numbers_grid), len(numbers_grid[0])

        for column_index in range(column_count -2, -1, -1):    
            numbers_grid[row_count -1][column_index] += numbers_grid[row_count -1][column_index +1]

        for row_index in range(row_count -2, -1, -1):    
            numbers_grid[row_index][column_count -1] += numbers_grid[row_index +1][column_count -1]

        for row_index in range(row_count -2, -1, -1):
            for column_index in range(column_count -2, -1, -1):

                numbers_grid[row_index][column_index] += \
                    min(numbers_grid[row_index][column_index +1], numbers_grid[row_index +1][column_index])
                
        return numbers_grid[0][0]
