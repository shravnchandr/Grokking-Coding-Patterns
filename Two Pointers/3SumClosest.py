from typing import List


class Solution:
    def threeSumClosest(self, numbers_list: List[int], target: int) -> int:
        closest_sum, closest_diff = float('inf'), float('inf')
        numbers_list_length = len(numbers_list)

        numbers_list = sorted(numbers_list)

        index = 0
        while index < numbers_list_length:
            value = numbers_list[index]

            left_index, right_index = index +1, numbers_list_length -1
            while left_index < right_index:
                left_value, right_value = numbers_list[left_index], numbers_list[right_index]

                current_sum = left_value + value + right_value
                current_diff = abs(target - current_sum)

                if current_diff < closest_diff:
                    closest_sum, closest_diff = current_sum, current_diff

                if current_sum <= target:
                    left_index = left_index +1

                elif current_sum > target:
                    right_index = right_index -1

            index = index +1

        return closest_sum