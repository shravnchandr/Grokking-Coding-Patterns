from typing import List


class Solution:
    def findMaxAverage(self, numbers_list: List[int], window_size: int) -> float:
        moving_sum = sum(numbers_list[:window_size])
        max_sum = moving_sum

        left_index, right_index = 0, window_size
        while right_index < len(numbers_list):
            moving_sum = -numbers_list[left_index] + moving_sum + numbers_list[right_index]
            max_sum = max(moving_sum, max_sum)

            left_index, right_index = left_index +1, right_index +1

        return max_sum / window_size
    

        