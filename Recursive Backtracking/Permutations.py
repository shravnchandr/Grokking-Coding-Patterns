from typing import List


class Solution:
    def permute(self, numbers_list: List[int]) -> List[List[int]]:
        permute_list = list()

        def helperFunction(index: int, current_list: List[int]) -> None:
            if len(current_list) == len(numbers_list):
                permute_list.append(current_list[:])
                return
            
            while index < len(numbers_list):
                current_list.append(numbers_list[index])
                helperFunction(index +1, current_list)
                current_list.pop()

        for index, number in enumerate(numbers_list):
            helperFunction([number])

        return permute_list


        