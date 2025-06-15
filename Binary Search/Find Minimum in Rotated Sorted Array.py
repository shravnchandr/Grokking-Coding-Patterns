from typing import List


class Solution:
    def findMin(self, numbers_list: List[int]) -> int:
        left_index, right_index = 0, len(numbers_list) -1
        while left_index <= right_index:
            middle_index = (left_index + right_index) // 2

            if numbers_list[left_index] > numbers_list[right_index]:
                if numbers_list[middle_index] < numbers_list[right_index]:
                    right_index = middle_index
                else:
                    left_index = middle_index +1

            else:
                right_index = middle_index -1

        return numbers_list[left_index]