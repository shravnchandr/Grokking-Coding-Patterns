from typing import List


class Solution:
    def calculateMinimumHP(self, dungeon_matrix: List[List[int]]) -> int:
        row_count, column_count = len(dungeon_matrix), len(dungeon_matrix[0])

        cell_value = dungeon_matrix[row_count -1][column_count - 1]
        if cell_value > 0:
            dungeon_matrix[row_count -1][column_count - 1] = 0
        else:
            dungeon_matrix[row_count -1][column_count - 1] = abs(cell_value) +1


        for row_index in range(row_count -2, -1, -1):
            cell_value = dungeon_matrix[row_index][column_count -1]
            if cell_value > 0:
                dungeon_matrix[row_index][column_count -1] = 0
            else:
                dungeon_matrix[row_index][column_count -1] = abs(cell_value) +1

            if row_index < row_count -1:
                dungeon_matrix[row_index][column_count -1] += dungeon_matrix[row_index +1][column_count -1]

        for column_index in range(column_count -2, -1, -1):
            cell_value = dungeon_matrix[row_count -1][column_index]
            if cell_value > 0:
                dungeon_matrix[row_count -1][column_index] = 0
            else:
                dungeon_matrix[row_count -1][column_index] = abs(cell_value) +1

            if column_index < column_count -1:
                dungeon_matrix[row_count -1][column_index] += dungeon_matrix[row_count -1][column_index +1]


        print(dungeon_matrix)

        
solution_object = Solution()
question = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
answer = solution_object.calculateMinimumHP(question)

