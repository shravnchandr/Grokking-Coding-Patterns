from typing import List


class Solution:
    def change(self, amount: int, coins_list: List[int]) -> int:        
        count_list = [0] * (amount +1)
        count_list[0] = 1

        for coin in coins_list:
            for amt in range(coin, amount +1):
                count_list[amt] = count_list[amt] + count_list[amt - coin]

        return count_list[amount]
    