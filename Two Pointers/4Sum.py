from typing import List


class Solution:
    def threeSum(self, numbers_list: List[int], target: int) -> List[List[int]]:
        numbers_list = sorted(numbers_list)
        numbers_list_length = len(numbers_list)

        return_list = list()

        index = 0
        while index < numbers_list_length -1:
            value = numbers_list[index]

            left_index, right_index = index +1, numbers_list_length -1

            while left_index < right_index:
                left_value, right_value = numbers_list[left_index], numbers_list[right_index]
                current_sum = left_value + value + right_value

                if current_sum == target:
                    return_list.append([left_value, value, right_value])

                    left_index, right_index = left_index +1, right_index -1
                    while left_index < right_index and numbers_list[left_index] == left_value:
                        left_index = left_index +1

                elif current_sum > target:
                    right_index = right_index -1
                elif current_sum < target:
                    left_index = left_index +1

            index = index +1
            while index < numbers_list_length -1 and numbers_list[index] == value:
                index = index +1


        return return_list
    

    def fourSum(self, numbers_list: List[int], target: int) -> List[List[int]]:
        numbers_list = sorted(numbers_list)
        numbers_list_length = len(numbers_list)

        return_list = list()

        index = 0
        while index < numbers_list_length -1:
            value = numbers_list[index]

            three_sum_list = self.threeSum(numbers_list= numbers_list[index +1:], target=target - value)
            final_list = list()

            for sum_list in three_sum_list:
                sum_list.append(value)
                final_list.append(sum_list)

            return_list.extend(final_list)

            index = index +1
            while index < numbers_list_length -1 and numbers_list[index] == value:
                index = index +1


        return return_list
