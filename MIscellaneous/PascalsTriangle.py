from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal_triangle = [[1] * (index +1) for index in range(numRows)]

        for row in range(2, numRows):
            for index in range(1, len(pascal_triangle[row]) -1):
                
                pascal_triangle[row][index] = pascal_triangle[row -1][index -1] + pascal_triangle[row -1][index]

        return pascal_triangle