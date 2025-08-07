from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacle_grid: List[List[int]]) -> int:
        row_count, column_count = len(obstacle_grid), len(obstacle_grid[0])

        path_count_grid = [[0] * column_count for _ in range(row_count)]
        path_count_grid[row_count -1][column_count -1] = 1 if obstacle_grid[row_count -1][column_count -1] != 1 else 0

        for column_index in range(column_count -2, -1, -1):    
            if obstacle_grid[row_count -1][column_index] == 1:
                path_count_grid[row_count -1][column_index] = 0
            else:
                path_count_grid[row_count -1][column_index] = path_count_grid[row_count -1][column_index +1]

        for row_index in range(row_count -2, -1, -1):    
            if obstacle_grid[row_index][column_count -1] == 1:
                path_count_grid[row_index][column_count -1] = 0
            else:
                path_count_grid[row_index][column_count -1] = path_count_grid[row_index +1][column_count -1]
        
        for row_index in range(row_count -2, -1, -1):
            for column_index in range(column_count -2, -1, -1):

                if obstacle_grid[row_index][column_index] == 1:
                    path_count_grid[row_index][column_index] = 0

                else:
                    down_count = path_count_grid[row_index +1][column_index]
                    right_count = path_count_grid[row_index][column_index +1]
                    path_count_grid[row_index][column_index] = down_count + right_count

        return path_count_grid[0][0]
        