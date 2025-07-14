import heapq
from typing import List


class Solution:
    def swimInWater(self, elevation_grid: List[List[int]]) -> int:
        grid_size = len(elevation_grid)

        min_elevation_heap = [(elevation_grid[0][0], 0, 0)]
        max_elevation = 0

        visited_elevations = set()
        directions = ((0,1), (1,0), (0,-1), (-1,0))

        while min_elevation_heap:
            elevation, row_index, column_index = heapq.heappop(min_elevation_heap)

            visited_elevations.add(elevation)
            max_elevation = max(max_elevation, elevation)

            if elevation == elevation_grid[-1][-1]:
                break

            for next_row, next_column in directions:
                new_row, new_column = row_index + next_row, column_index + next_column

                if 0<= new_row < grid_size and 0 <= new_column < grid_size:
                    new_elevation = elevation_grid[new_row][new_column]

                    if new_elevation not in visited_elevations:
                        heapq.heappush(min_elevation_heap, (new_elevation, new_row, new_column))

        return max_elevation
    