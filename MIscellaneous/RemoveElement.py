from typing import List


class Solution:
    def removeElement(self, numbers_list: List[int], remove_value: int) -> int:
        left_index, right_index = 0, len(numbers_list) -1

        while left_index < right_index:
            if numbers_list[left_index] == remove_value:
                numbers_list[left_index], numbers_list[right_index] = numbers_list[right_index], numbers_list[left_index]

                right_index = right_index -1
            
            else:
                left_index = left_index +1

        return_count = 0
        for value in numbers_list:
            if value != remove_value:
                return_count = return_count +1

        return return_count
            