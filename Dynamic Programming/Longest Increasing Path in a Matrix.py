from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        row_count, column_count = len(matrix), len(matrix[0])
        directions = ((0,1), (1,0), (0,-1), (-1,0))

        dp_memoization = {}
        def depth_first_search(row_index: int, column_index: int, previous_value: int) -> int:
            if (row_index, column_index, previous_value) in dp_memoization:
                return dp_memoization[(row_index, column_index, previous_value)]

            max_length = 1            
            for row_dir, column_dir in directions:
                next_row, next_column = row_index + row_dir, column_index + column_dir

                if 0 <= next_row < row_count and 0 <= next_column < column_count and \
                    matrix[next_row][next_column] > matrix[row_index][column_index]:

                    path_length = 1 + depth_first_search(next_row, next_column, matrix[row_index][column_index])
                    max_length = max(path_length, max_length)

            dp_memoization[(row_index, column_index, previous_value)] = max_length
            return dp_memoization[(row_index, column_index, previous_value)]
        
        return_length = 0
        for row_index in range(row_count):
            for column_index in range(column_count):
                
                current_length = depth_first_search(row_index, column_index, float('-inf'))
                return_length = max(current_length, return_length)

        return return_length
