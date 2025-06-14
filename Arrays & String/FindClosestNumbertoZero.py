from typing import List


class Solution:
    def findClosestNumber(self, numbers_list: List[int]) -> int:
        closest_number, abs_diff = float('inf'), float('inf')

        for number in numbers_list:
            if abs(number) < abs_diff:
                closest_number = number
                abs_diff = abs(number)
                
            elif abs(number) == abs_diff:
                closest_number = max(number ,closest_number)

        return closest_number
    