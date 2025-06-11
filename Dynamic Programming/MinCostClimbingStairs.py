from typing import List


class Solution:
    def minCostClimbingStairs(self, cost_list: List[int]) -> int:
        dp_storage = [0] * (len(cost_list))
        dp_storage[0], dp_storage[1] = cost_list[0], cost_list[1]

        for index in range(2, len(cost_list)):
            dp_storage[index] = cost_list[index] + min(dp_storage[index-2:index])

        return min(dp_storage[-2:])
    