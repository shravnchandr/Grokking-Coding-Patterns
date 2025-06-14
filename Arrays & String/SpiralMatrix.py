from typing import List, Tuple


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        spiral_list = list()

        def traverseMatrix(row_index: int, column_index: int, count: int, direction: str) -> Tuple:
            
            if direction == 'right':    
                for _ in range(count):
                    spiral_list.append(matrix[row_index][column_index])
                    column_index = column_index +1

                return (row_index +1, column_index -1, 'down')
            
            if direction == 'left':
                for _ in range(count):
                    spiral_list.append(matrix[row_index][column_index])
                    column_index = column_index -1

                return (row_index -1, column_index +1, 'up')
            
            if direction == 'down':
                for _ in range(count):
                    spiral_list.append(matrix[row_index][column_index])
                    row_index = row_index +1

                return (row_index -1, column_index -1, 'left')
            
            if direction == 'up':
                for _ in range(count):
                    spiral_list.append(matrix[row_index][column_index])
                    row_index = row_index -1

                return (row_index +1, column_index +1, 'right')
            

        row_count, column_count = len(matrix[0]), len(matrix) -1
        row_index, column_index = 0, 0
        direction = 'right'

        while len(spiral_list) < len(matrix) * len(matrix[0]):
            row_index, column_index, direction = traverseMatrix(row_index, column_index, row_count, direction)
            row_index, column_index, direction = traverseMatrix(row_index, column_index, column_count, direction)

            row_count, column_count = row_count -1, column_count -1

        return spiral_list