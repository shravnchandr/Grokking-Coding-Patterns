import heapq
from typing import List


class Solution:
    def kClosest(self, points_list: List[List[int]], k_index: int) -> List[List[int]]:
        
        distance_list = [point[0] **2 + point[1] **2 for point in points_list]
        distance_mapping = dict()

        for point,distance in zip(points_list, distance_list):
            if distance in distance_mapping:
                distance_mapping[distance].append(point)
            else:
                distance_mapping[distance] = [point]

        closest_points = list()
        heapq.heapify(distance_list)

        while len(closest_points) < k_index:
            current_points = distance_mapping[heapq.heappop(distance_list)]
            closest_points.extend(current_points)

        return closest_points
       

        