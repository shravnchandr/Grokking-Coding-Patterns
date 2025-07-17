from typing import List


class UnionFind:
    def __init__(self, size: int):
        self.parent = [i for i in range(size)]
        self.rank = [0] * size 

    def find(self, node: int) -> int:
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, node1: int, node2: int) -> bool:
        root1 = self.find(node1)
        root2 = self.find(node2)

        if root1 == root2:
            return False

        if self.rank[root1] < self.rank[root2]:
            self.parent[root1] = root2
        elif self.rank[root1] > self.rank[root2]:
            self.parent[root2] = root1
        else:
            self.parent[root2] = root1
            self.rank[root1] += 1

        return True


class Solution:
    def countComponents(self, nodes_count: int, edges_list: List[List[int]]) -> int:
        union_find = UnionFind(nodes_count)

        for source, destination in edges_list:
            union_find.union(source, destination)

        parent_nodes = set()
        for node in nodes_count:
            parent_nodes.add(union_find.parent(node))

        return len(parent_nodes)
    