from typing import List


class Solution:
    def permute(self, numbers_list: List[int]) -> List[List[int]]:
        permute_list = list()

        def helperFunction(current_list: List[int]) -> None:
            if len(current_list) == len(numbers_list):
                permute_list.append(current_list[:])
                return
            
            for number in numbers_list:
                if number not in current_list:
                    current_list.append(number)
                    helperFunction(current_list)
                    current_list.pop()

        helperFunction()
        return permute_list
        