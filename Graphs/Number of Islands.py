from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def helperFunction(row_index: int, column_index: int) -> None:
            if row_index < 0 or row_index >= len(grid) or column_index < 0 or column_index >= len(grid[0]):
                return 
            if grid[row_index][column_index] == '0':
                return
            
            grid[row_index][column_index] = '0'

            helperFunction(row_index -1, column_index)
            helperFunction(row_index +1, column_index)
            helperFunction(row_index, column_index -1)
            helperFunction(row_index, column_index +1)

        island_count = 0
        for row_index in range(len(grid)):
            for column_index in range(len(grid[0])):

                if grid[row_index][column_index] == '1':
                    island_count = island_count +1
                    helperFunction(row_index, column_index)

        return island_count
    
