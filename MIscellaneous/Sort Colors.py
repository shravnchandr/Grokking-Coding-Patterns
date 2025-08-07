from collections import Counter
from typing import List


class Solution:
    def sortColors(self, numbers_list: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        color_count = Counter(numbers_list)
        index_dict = {
            0: 0,
            1: color_count[0],
            2: color_count[0] + color_count[1],
        }

        for color, color_index in index_dict.items():
            index = 0

            while index < len(numbers_list):
                if numbers_list[index] == color:
                    numbers_list[color_index], numbers_list[index] = numbers_list[index], numbers_list[color_index]
                    color_index = color_index +1

                index = index +1
