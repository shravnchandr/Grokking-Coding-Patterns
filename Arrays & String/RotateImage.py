from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        left_index, right_index = 0, len(matrix) -1

        while left_index < right_index:
            for index in range(right_index - left_index):

                value = matrix[left_index][left_index + index]

                matrix[left_index][left_index + index] = matrix[right_index -index][left_index]
                matrix[right_index -index][left_index] = matrix[right_index][right_index - index]
                matrix[right_index][right_index - index] = matrix[left_index + index][right_index]

                matrix[left_index + index][right_index] = value

            left_index, right_index = left_index +1, right_index -1


        for row_index in range(len(matrix)):
            for column_index in range(row_index +1, len(matrix)):
                matrix[row_index][column_index], matrix[column_index][row_index] = matrix[column_index][row_index], matrix[row_index][column_index]

        for row_index in range(len(matrix)):
            for column_index in range(len(matrix) // 2):
                matrix[row_index][column_index], matrix[row_index][len(matrix) -1 - column_index] = matrix[row_index][len(matrix) -1 - column_index], matrix[row_index][column_index]
