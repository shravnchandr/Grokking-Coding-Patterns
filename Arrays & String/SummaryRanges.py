from typing import List


class Solution:
    def summaryRanges(self, numbers_list: List[int]) -> List[str]:
        summary_list = list()

        left_index, right_index = 0, 0
        while right_index < len(numbers_list):
            while right_index < len(numbers_list) and numbers_list[left_index] + (right_index - left_index) == numbers_list[right_index]:
                right_index = right_index +1

            if numbers_list[left_index] == numbers_list[right_index -1]:
                summary_list.append(f"{numbers_list[left_index]}")
            else:
                summary_list.append(f"{numbers_list[left_index]}->{numbers_list[right_index -1]}")

            left_index = right_index
            right_index = right_index +1

        if left_index == len(numbers_list) -1:
            summary_list.append(f"{numbers_list[left_index]}")

        return summary_list
            