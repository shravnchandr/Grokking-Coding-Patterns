from typing import List


class Solution:
    def removeDuplicates(self, numbers_list: List[int]) -> int:
        left_index, right_index = 0, 1
        unique_numbers = 0

        while right_index < len(numbers_list):
            
            if numbers_list[left_index] != numbers_list[right_index]:
                unique_numbers = unique_numbers +1
                left_index = left_index +1
                numbers_list[left_index] = numbers_list[right_index]
                
            right_index = right_index +1

        return unique_numbers