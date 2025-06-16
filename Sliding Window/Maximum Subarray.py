from typing import List


class Solution:
    def maxSubArray(self, numbers_list: List[int]) -> int:
        current_sum, max_sum = 0, sum(numbers_list)
        left_index, right_index = 0, 0

        while right_index < len(numbers_list):
            current_sum = current_sum + numbers_list[right_index]
            max_sum = max(current_sum, max_sum)

            while left_index <= right_index and current_sum < 0:
                current_sum = current_sum - numbers_list[left_index]
                left_index = left_index +1

            right_index = right_index +1

        return max_sum
