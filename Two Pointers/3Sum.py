from typing import List


class Solution:
    def threeSum(self, numbers_list: List[int]) -> List[List[int]]:
        numbers_list = sorted(numbers_list)
        numbers_list_length = len(numbers_list)

        return_list = list()

        index = 0
        while index < numbers_list_length -1:
            value = numbers_list[index]

            if value > 0:
                break

            left_index, right_index = index +1, numbers_list_length -1

            while left_index < right_index:
                left_value, right_value = numbers_list[left_index], numbers_list[right_index]
                current_sum = left_value + value + right_value

                if current_sum == 0:
                    return_list.append([left_value, value, right_value])

                    left_index, right_index = left_index +1, right_index -1
                    while left_index < right_index and numbers_list[left_index] == left_value:
                        left_index = left_index +1

                elif current_sum > 0:
                    right_index = right_index -1
                elif current_sum < 0:
                    left_index = left_index +1

            index = index +1
            while index < numbers_list_length -1 and numbers_list[index] == value:
                index = index +1


        return return_list