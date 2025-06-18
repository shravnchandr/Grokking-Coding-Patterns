from collections import defaultdict
import heapq
from typing import List


class Solution:
    def networkDelayTime(self, times_list: List[List[int]], node_count: int, source_node: int) -> int:

        time_mapping = defaultdict(list)
        for source, destination, travel_time in times_list:
            time_mapping[source].append((travel_time, destination))

        time_min_heap = [(0, source_node)]
        visited_node = set()

        min_time = dict()
        min_time[source_node] = 0
        
        while time_min_heap:
            travel_time, current_node = heapq.heappop(time_min_heap)

            if current_node in visited_node:
                continue

            visited_node.add(current_node)
            min_time[current_node] = travel_time

            for next_time, next_node in time_mapping[current_node]:
                if next_node not in visited_node:
                    heapq.heappush(time_min_heap, (travel_time + next_time, next_node))

        if len(visited_node) == node_count:
            return max(min_time.values())
        
        return -1
    