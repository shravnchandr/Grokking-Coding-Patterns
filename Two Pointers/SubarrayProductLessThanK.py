from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, numbers_list: List[int], target: int) -> int:
        if target < 2:
            return 0

        array_count, array_product = 0, 1
        left_index, right_index = 0, 0

        while right_index < len(numbers_list):
            array_product = numbers_list[right_index] * array_product

            while array_product >= target:
                array_product = array_product // numbers_list[left_index]
                left_index = left_index +1

            array_count = array_count + (right_index - left_index) +1

            right_index = right_index +1

        return array_count
    