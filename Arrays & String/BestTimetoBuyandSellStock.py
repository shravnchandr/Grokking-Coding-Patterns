from typing import List


class Solution:
    def maxProfit(self, prices_list: List[int]) -> int:
        max_profit, buy_price = 0, prices_list[0]

        index = 1
        while index < len(prices_list):
            price = prices_list[index]

            if price < buy_price:
                buy_price = price
            else:
                max_profit = max(max_profit, price - buy_price)

        return max_profit