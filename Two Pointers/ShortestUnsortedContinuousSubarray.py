from typing import List


class Solution:
    def findUnsortedSubarray(self, numbers_list: List[int]) -> int:
        numbers_list_length = len(numbers_list)

        current_max, current_min = numbers_list[0], numbers_list[-1]
        start_index, end_index = 0, 0

        for index in range(1, numbers_list_length):
            value = numbers_list[index]
            current_max = max(value, current_max)

            if value < current_max:
                end_index = index

        for reverse_index in range(numbers_list_length -2, -1, -1):
            # reverse_index = numbers_list_length - index +1
            value = numbers_list[reverse_index]
            current_min = min(value, current_min)

            if value > current_min:
                start_index = reverse_index

        return end_index - start_index +1