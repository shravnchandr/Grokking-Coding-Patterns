import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones_weight: List[int]) -> int:
        stones_weight = [-stone for stone in stones_weight]

        heapq.heapify(stones_weight)

        while len(stones_weight) > 1:
            big_stone_1 = heapq.heappop(stones_weight)
            big_stone_2 = heapq.heappop(stones_weight)
            heapq.heappush(stones_weight, big_stone_1 - big_stone_2)

        return -heapq.heappop(stones_weight) if stones_weight else 0 
        