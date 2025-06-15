from typing import List


class Solution:
    def trap(self, height_list: List[int]) -> int:
        left_max, right_max = [0] * len(height_list), [0] * len(height_list)

        left_max_value, right_max_value = height_list[0], height_list[-1]
        for index in range(1, len(height_list)):
            left_max[index] = left_max_value
            left_max_value = max(height_list[index], left_max_value)

        
            right_max[len(height_list) - index -2] = right_max_value
            right_max_value = max(height_list[len(height_list) - index -2], right_max_value)

        total_water = 0
        for index in range(len(height_list)):
            trap_water = min(left_max[index], right_max[index]) - height_list[index]

            if trap_water > 0:
                total_water = total_water + trap_water

        return total_water

