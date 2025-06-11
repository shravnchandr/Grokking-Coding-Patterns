from typing import List


class Solution:
    def rob(self, cost_list: List[int]) -> int:
        if len(cost_list) < 2:
            return cost_list[0]
         
        dp_storage = [0] * (len(cost_list))
        dp_storage[0], dp_storage[1] = cost_list[0], max(cost_list[0], cost_list[1])

        for index in range(2, len(cost_list)):  
            dp_storage[index] = max(dp_storage[index -1], cost_list[index] + dp_storage[index -2])


        return dp_storage[len(cost_list) -1]