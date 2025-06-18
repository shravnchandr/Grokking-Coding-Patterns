from collections import deque
from typing import Optional


class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, start_node: Optional['Node']) -> Optional['Node']:
        if not start_node:
            return None
        
        node_queue = deque()
        node_queue.append(start_node)

        visited_nodes = set()
        visited_nodes.add(start_node)

        old_new_map = dict()
        while node_queue:
            current_node = node_queue.popleft()
            old_new_map[current_node] = Node(current_node.val)

            for neighbor_node in current_node.neighbors:
                if neighbor_node not in visited_nodes:
                    visited_nodes.add(neighbor_node)
                    node_queue.append(neighbor_node)

        for old_node, new_node in old_new_map.items():
            for neighbor_node in old_node.neighbors:
                new_node.neighbors.append(old_new_map[neighbor_node])

        return old_new_map[start_node]

        