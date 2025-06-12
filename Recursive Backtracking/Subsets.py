from typing import List


class Solution:
    def subsets(self, numbers_list: List[int]) -> List[List[int]]:
        final_list, current_list = list(), list()

        def helper_function(index: int):
            if index == len(numbers_list):
                final_list.append(current_list[:])
                return
            
            current_list.append(numbers_list[index])
            for jndex in range(index +1, len(numbers_list)):
                helper_function(jndex)

            final_list.append(current_list[:])
            current_list.pop()

        for index in range(len(numbers_list)):
            helper_function(index)

        final_list.appen([])
        return final_list
        
