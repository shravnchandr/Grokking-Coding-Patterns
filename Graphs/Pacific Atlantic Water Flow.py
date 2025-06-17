from collections import deque
from typing import List


class Solution:
    def pacificAtlantic(self, heights_matrix: List[List[int]]) -> List[List[int]]:
        IMPOSSIBLE, CHECKING, POSSIBLE = 0, 1, 2

        altantic_grid = [[-1] * len(heights_matrix[0]) for _ in range(len(heights_matrix))]
        for row_index in range(len(heights_matrix)):
            for column_index in range(len(heights_matrix[0])):
                if row_index == len(heights_matrix) -1 or column_index == len(heights_matrix[0]) -1:
                    altantic_grid[row_index][column_index] = POSSIBLE

        def flowAtlantic(row_index: int, column_index: int, previous_height: int) -> bool:
            if row_index < 0 or column_index < 0 or row_index >= len(heights_matrix) or column_index >= len(heights_matrix[0]):
                return False
            if heights_matrix[row_index][column_index] > previous_height:
                return False
            if altantic_grid[row_index][column_index] == CHECKING:
                return False

            if altantic_grid[row_index][column_index] == POSSIBLE:
                return True

            altantic_grid[row_index][column_index] = CHECKING
            current_height = heights_matrix[row_index][column_index]

            up_flow = flowAtlantic(row_index -1, column_index, current_height)
            down_flow = flowAtlantic(row_index +1, column_index, current_height)
            left_flow = flowAtlantic(row_index, column_index -1, current_height)
            right_flow = flowAtlantic(row_index, column_index +1, current_height)

            flow_possible = left_flow or right_flow or up_flow or down_flow
            altantic_grid[row_index][column_index] = POSSIBLE if flow_possible else IMPOSSIBLE

            return flow_possible

        pacific_grid = [[-1] * len(heights_matrix[0]) for _ in range(len(heights_matrix))]
        for row_index in range(len(heights_matrix)):
            for column_index in range(len(heights_matrix[0])):
                if row_index == 0 or column_index == 0:
                    pacific_grid[row_index][column_index] = POSSIBLE

        def flowPacific(row_index: int, column_index: int, previous_height: int) -> bool:
            if row_index < 0 or column_index < 0 or row_index >= len(heights_matrix) or column_index >= len(heights_matrix[0]):
                return False
            if heights_matrix[row_index][column_index] > previous_height:
                return False
            if pacific_grid[row_index][column_index] == CHECKING:
                return False

            if pacific_grid[row_index][column_index] == POSSIBLE:
                return True

            pacific_grid[row_index][column_index] = CHECKING
            current_height = heights_matrix[row_index][column_index]

            up_flow = flowPacific(row_index -1, column_index, current_height)
            down_flow = flowPacific(row_index +1, column_index, current_height)
            left_flow = flowPacific(row_index, column_index -1, current_height)
            right_flow = flowPacific(row_index, column_index +1, current_height)

            flow_possible = left_flow or right_flow or up_flow or down_flow
            pacific_grid[row_index][column_index] = POSSIBLE if flow_possible else IMPOSSIBLE

            return flow_possible

        flow_cells = list()
        for row_index in range(len(heights_matrix)):
            for column_index in range(len(heights_matrix[0])):

                current_height = heights_matrix[row_index][column_index]
                atlantic_flow = flowAtlantic(row_index, column_index, current_height)
                pacific_flow = flowPacific(row_index, column_index, current_height)

                if atlantic_flow and pacific_flow:
                    flow_cells.append([row_index, column_index])

        return flow_cells


    def pacificAtlantic(self, heights_matrix: List[List[int]]) -> List[List[int]]:
        row_count, column_count = len(heights_matrix), len(heights_matrix[0])

        pacific_reachable, atlantic_reachable = set(), set()
        pacific_queue, atlantic_queue = deque(), deque()

        for row_index in range(row_count):
            pacific_reachable.add((row_index, 0))
            atlantic_reachable.add((row_index, column_count -1))

            pacific_queue.append((row_index, 0))
            atlantic_queue.append((row_index, column_count -1))

        for column_index in range(column_count):
            pacific_reachable.add((0, column_index))
            atlantic_reachable.add((row_count -1, column_index))

            pacific_queue.append((0, column_index))
            atlantic_queue.append((row_count -1, column_index))

        directions = ((0,1), (0,-1), (1,0), (-1,0))

        def breadthFirstSearch(queue: deque, reachable_set: set):
            while queue:
                row_index, column_index = queue.popleft()

                for row_direction,column_direction in directions:
                    next_row, next_column = row_index + row_direction, column_index + column_direction

                    if 0 <= next_row < row_count and 0 <= next_column < column_count:
                        current_height, next_height = heights_matrix[row_index][column_index], heights_matrix[next_row][next_column]
                        
                        if (next_row, next_column) not in reachable_set and next_height >= current_height:
                            reachable_set.add((next_row, next_column))
                            queue.append((next_row, next_column))

        breadthFirstSearch(pacific_queue, pacific_reachable)
        breadthFirstSearch(atlantic_queue, atlantic_reachable)

        flow_cells = list()
        for row_index in range(row_count):
            for column_index in range(column_count):
                if (row_index, column_index) in pacific_reachable and (row_index, column_index) in atlantic_reachable:
                    flow_cells.append([row_index, column_index])

        return flow_cells
