from collections import defaultdict, deque
from typing import List


class Solution:
    def validPath(self, node_count: int, edges: List[List[int]], source: int, destination: int) -> bool:
        node_map = defaultdict(set)
        for node_x, node_y in edges:
            node_map[node_x].add(node_y)
            node_map[node_y].add(node_x)

        node_queue = deque()
        node_queue.append(source)
        seen_node = set()
        seen_node.add(source)

        while node_queue:
            current_node = node_queue.popleft()

            if current_node == destination:
                return True
            
            for node in node_map[current_node]:
                if node not in seen_node:
                    seen_node.add(node)
                    node_queue.append(node)

        return False
    