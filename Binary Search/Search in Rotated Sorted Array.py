from typing import List


class Solution:
    def search(self, numbers_list: List[int], target: int) -> int:
        left_index, right_index = 0, len(numbers_list) -1
        while left_index <= right_index:
            middle_index = (left_index + right_index) // 2

            if numbers_list[middle_index] == target:
                return middle_index
            
            if numbers_list[left_index] <= numbers_list[middle_index]:
                if target < numbers_list[left_index] or target > numbers_list[middle_index]:
                    left_index = middle_index +1
                else:
                    right_index = right_index -1

            elif numbers_list[middle_index] < numbers_list[right_index]:
                if target > numbers_list[right_index] or target < numbers_list[middle_index]:
                    right_index = middle_index -1
                else:
                    left_index = middle_index +1

        return -1