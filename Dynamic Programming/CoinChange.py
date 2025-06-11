from typing import List


class Solution:
    def coinChange(self, coins_list: List[int], amount: int) -> int:
        count_list = [float('inf')] * (amount +1)
        count_list[0] = 0

        for amt in range(amount +1):
            for coin in coins_list:

                differnce = amt - coin
                if differnce >=0 and count_list[differnce] != float('inf'):
                    count_list[amt] = min(count_list[amt], count_list[differnce] +1)

           
        return count_list[amount] if count_list[amount] != float('inf') else -1