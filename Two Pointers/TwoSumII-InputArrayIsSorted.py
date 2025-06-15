from typing import List


class Solution:
    def twoSum(self, numbers_list: List[int], target_sum: int) -> List[int]:

        left_index, right_index = 0, len(numbers_list) -1
        while left_index < right_index:
            current_sum = numbers_list[left_index] + numbers_list[right_index]

            if current_sum < target_sum:
                left_index = left_index +1
            elif current_sum > target_sum:
                right_index = right_index -1
            else:
                return [left_index +1, right_index +1]

        