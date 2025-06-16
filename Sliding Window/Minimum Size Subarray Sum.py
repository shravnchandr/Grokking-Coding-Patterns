from typing import List


class Solution:
    def minSubArrayLen(self, target: int, numbers_list: List[int]) -> int:
        if sum(numbers_list) < target:
            return 0

        current_sum, min_length = 0, len(numbers_list)
        left_index, right_index = 0, 0

        while right_index < len(numbers_list):
            current_sum = current_sum + numbers_list[right_index]

            while left_index <= right_index and current_sum - numbers_list[left_index] >= target:
                    current_sum = current_sum - numbers_list[left_index]
                    left_index = left_index +1

            if current_sum >= target:
                min_length = min(right_index - left_index +1, min_length)

            right_index = right_index +1

        return min_length
    