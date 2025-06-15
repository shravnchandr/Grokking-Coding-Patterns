import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles_list: List[int], hours: int) -> int:
        left_index, right_index = 1, max(piles_list)

        while left_index <= right_index:
            middle_index = (left_index + right_index) // 2
            eat_hours = sum([math.ceil(pile/middle_index) for pile in piles_list])

            if eat_hours > hours:
                left_index = middle_index +1
            else:
                right_index = middle_index -1

        return left_index
