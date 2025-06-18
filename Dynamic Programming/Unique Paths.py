class Solution:
    def uniquePaths(self, row_count: int, column_count: int) -> int:
        grid = [[0] * column_count for _ in range(row_count)]

        for row_index in range(row_count):
            grid[row_index][column_count -1] = 1
        for column_index in range(column_count):
            grid[row_count -1][column_index] = 1

        for row_index in range(row_count -2, -1, -1):
            for column_index in range(column_count -2, -1, -1):
                grid[row_index][column_index] = grid[row_index][column_index +1] + grid[row_index +1][column_index]

        return grid[0][0]
        