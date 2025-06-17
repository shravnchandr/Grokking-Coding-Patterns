from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def helperFunction(row_index: int, column_index: int) -> int:
            if row_index < 0 or row_index >= len(grid) or column_index < 0 or column_index >= len(grid[0]):
                return 0
            if grid[row_index][column_index] == 0:
                return 0
            
            grid[row_index][column_index] = 0

            left_area = helperFunction(row_index -1, column_index)
            right_area = helperFunction(row_index +1, column_index)
            up_area = helperFunction(row_index, column_index -1)
            down_area = helperFunction(row_index, column_index +1)

            return 1 + left_area + right_area + up_area + down_area

        max_area = 0
        for row_index in range(len(grid)):
            for column_index in range(len(grid[0])):

                if grid[row_index][column_index] == 1:
                    current_area = helperFunction(row_index, column_index)
                    max_area = max(current_area, max_area)

        return max_area
    
