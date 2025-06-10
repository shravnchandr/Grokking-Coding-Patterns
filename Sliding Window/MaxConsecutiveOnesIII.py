from collections import defaultdict
from typing import List


class Solution:
    def longestOnes(self, numbers_list: List[int], replace_count: int) -> int:
        max_length, zero_count = 0, 0
        left_index, right_index = 0, 0

        while right_index < len(numbers_list):
            right_char = numbers_list[right_index]
            if right_char == 0:
                zero_count = zero_count +1

            while zero_count > replace_count:
                left_char = numbers_list[left_index]
                if left_char == 0:
                    zero_count = zero_count -1

                left_index = left_index +1

            max_length = max(right_index - left_index +1, max_length)
            right_index = right_index +1

        max_length = max(right_index - left_index, max_length)
        return max_length

        