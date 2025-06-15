from typing import List


class Solution:
    def searchInsert(self, numbers_list: List[int], target: int) -> int:
        left_index, right_index = 0, len(numbers_list) -1
        while left_index <= right_index:
            middle_index = (left_index + right_index) // 2

            if numbers_list[middle_index] < target:
                left_index = middle_index +1
            elif numbers_list[middle_index] > target:
                right_index = middle_index -1
            else:
                return middle_index

        return left_index

        