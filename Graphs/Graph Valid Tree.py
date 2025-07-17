from collections import defaultdict, deque
from typing import List


class Solution:
    def validTree(self, nodes_count: int, edges_list: List[List[int]]) -> bool:

        node_map = defaultdict(list)
        for source, destination in edges_list:
            node_map[source].append(destination)
            node_map[destination].append(source)

        visited_nodes = [False] * nodes_count
        
        nodes_queue = deque()
        nodes_queue.append((0, -1))

        while nodes_queue:
            current_node, parent_node = nodes_queue.popleft()

            if visited_nodes[current_node]:
                return False
            visited_nodes[current_node] = True

            for neighbor in node_map[current_node]:
                if neighbor != parent_node:
                    nodes_queue.append((neighbor, current_node))

        return all(visited_nodes)

        