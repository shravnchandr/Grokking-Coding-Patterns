from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle) == 1:
            return triangle[0][0]
        
        triangle[1][0] += triangle[0][0]
        triangle[1][1] += triangle[0][0]
        
        for row_index in range(2, len(triangle)):
            for column_index in range(len(triangle[row_index])):

                if column_index == 0:
                    to_add = triangle[row_index -1][column_index]
                elif column_index == len(triangle[row_index]) -1:
                    to_add = triangle[row_index -1][column_index -1]
                else:
                    to_add = min(triangle[row_index -1][column_index], triangle[row_index -1][column_index -1]) 

                triangle[row_index][column_index] += to_add

        return min(triangle[-1])
    