from typing import List


class Solution:
    def maxArea(self, height_list: List[int]) -> int:
        max_area = 0
        left_index, right_index = 0, len(height_list) -1

        while left_index < right_index:
            max_area = max(min(height_list[left_index], height_list[right_index])*(right_index - left_index), max_area)

            if height_list[left_index] < height_list[right_index]:
                left_index = left_index +1
            else:
                right_index = right_index -1

        return max_area