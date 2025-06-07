from typing import List


class Solution:
    def sortedSquares(self, numbers_list: List[int]) -> List[int]:
        return_list = [0] * len(numbers_list)
        left_index, right_index = 0, len(numbers_list) -1

        for index in range(len(numbers_list)):
            left_value, right_value = numbers_list[left_index], numbers_list[right_index]

            if abs(left_value) < abs(right_value):
                return_list[index] = left_value ** 2
                left_index = left_index +1

            else:
                return_list[index] = right_value ** 2
                right_index = right_index -1

        return return_list
