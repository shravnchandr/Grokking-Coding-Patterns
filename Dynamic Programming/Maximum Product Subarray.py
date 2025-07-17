from typing import List


class Solution:
    def maxProduct(self, numbers_list: List[int]) -> int:
        max_product = numbers_list[0]
        current_min, current_max = numbers_list[0], numbers_list[0]

        for number in numbers_list[1:]:
            if number < 0:
                current_min, current_max = current_max, current_min

            current_max = max(number, current_max * number)
            current_min = min(number, current_min * number)

            max_product = max(current_max, max_product)

        return max_product

        