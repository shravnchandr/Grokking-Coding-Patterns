from typing import List


class Solution:
    def maxProfit(self, prices_list: List[int]) -> int:
        dp_memoization = {}

        def depth_first_search(index: int, buying: bool) -> int:
            if index >= len(prices_list):
                return 0
            
            if (index,buying) in dp_memoization:
                return dp_memoization[(index,buying)]
            
            cooldown_profit = depth_first_search(index +1, buying)

            if buying:
                buying_profit = depth_first_search(index +1, not buying) - prices_list[index]
                dp_memoization[(index,buying)] = max(buying_profit, cooldown_profit)
            else:
                selling_profit = depth_first_search(index +2, not buying) + prices_list[index]
                dp_memoization[(index,buying)] = max(selling_profit, cooldown_profit)

            return dp_memoization[(index,buying)]
    
        return depth_first_search(0, True)
    

    def maxProfit(self, prices_list: List[int]) -> int:

        dp_memoization = [[0] * 3 for _ in prices_list]

        dp_memoization[0][0] = -prices_list[0]
        dp_memoization[0][1], dp_memoization[0][2] = 0, 0

        for index in range(1, len(prices_list)):
            dp_memoization[index][0] = max(dp_memoization[index -1][0], dp_memoization[index -1][2] - prices_list[index])
            dp_memoization[index][1] = dp_memoization[index -1][0] + prices_list[index]
            dp_memoization[index][2] = max(dp_memoization[index -1][1], dp_memoization[index -1][2])

        return max(dp_memoization[-1][1], dp_memoization[-1][2])
        