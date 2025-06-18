from typing import List


class Solution:
    def old_rob(self, cost_list: List[int]) -> int:    
        dp_storage = [0] * (len(cost_list))
        dp_storage[0], dp_storage[1] = cost_list[0], max(cost_list[0], cost_list[1])

        for index in range(2, len(cost_list)):  
            dp_storage[index] = max(dp_storage[index -1], cost_list[index] + dp_storage[index -2])


        return dp_storage[len(cost_list) -1]

    def rob(self, cost_list: List[int]) -> int:
        if len(cost_list) < 3:
            return max(cost_list)

        return max(self.old_rob(cost_list[1:]), self.old_rob(cost_list[:-1]))