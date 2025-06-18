import heapq
from typing import List


class Solution:
    def minCostConnectPoints(self, points_list: List[List[int]]) -> int:
        distance_mapping = dict()
        for point in points_list:
            distance_mapping[tuple(point)] = float('inf')
        
        starting_point = tuple(points_list[0])
        distance_mapping[starting_point] = 0

        distance_min_heap = [(0, starting_point)]
        
        visited_point = set()
        total_cost = 0
        
        while len(visited_point) != len(points_list):
            current_cost, current_point = heapq.heappop(distance_min_heap)

            if current_point in visited_point:
                continue

            visited_point.add(current_point)
            total_cost = total_cost + current_cost

            for row,column in points_list:
                next_point = (row, column)
                next_cost = abs(next_point[0] - current_point[0]) + abs(next_point[1] - current_point[1])

                if next_point != current_point and next_cost < distance_mapping[next_point]:
                    distance_mapping[next_point] = next_cost
                    heapq.heappush(distance_min_heap, (next_cost, next_point))

        return total_cost
    

    def minCostConnectPoints(self, points_list: List[List[int]]) -> int:
        distance_min_heap = [(0, tuple(points_list[0]))]
        
        visited_point = set()
        total_cost = 0
        
        while len(visited_point) != len(points_list):
            current_cost, current_point = heapq.heappop(distance_min_heap)

            if current_point in visited_point:
                continue

            visited_point.add(current_point)
            total_cost = total_cost + current_cost

            for row,column in points_list:
                next_point = (row, column)
                next_cost = abs(next_point[0] - current_point[0]) + abs(next_point[1] - current_point[1])

                if next_point != current_point and next_point not in visited_point:
                    heapq.heappush(distance_min_heap, (next_cost, next_point))

        return total_cost
    