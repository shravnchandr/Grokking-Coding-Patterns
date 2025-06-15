from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left_index, right_index = 0, len(matrix) -1
        row_index = -1

        while left_index <= right_index:
            middle_index = (left_index + right_index) // 2

            if matrix[middle_index][0] < target:
                left_index = middle_index +1
            elif matrix[middle_index][0] > target:
                right_index = middle_index -1
            else:
                row_index = middle_index
                break

        row_index = left_index -1 if row_index == -1 else row_index

        left_index, right_index = 0, len(matrix[0]) -1
        while left_index <= right_index:
            middle_index = (left_index + right_index) // 2

            if matrix[row_index][middle_index] < target:
                left_index = middle_index +1
            elif matrix[row_index][middle_index] > target:
                right_index = middle_index -1
            else:
                return True

        return False 