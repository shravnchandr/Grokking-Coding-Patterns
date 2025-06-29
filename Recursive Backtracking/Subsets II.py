from typing import List


class Solution:
    def subsetsWithDup(self, numbers_list: List[int]) -> List[List[int]]:
        numbers_list.sort()
        final_list, current_list = list(), list()

        list_count = len(numbers_list)

        def recursive_backtracking(index: int):
            if index == list_count:
                final_list.append(current_list[:])
                return
            
            current_list.append(numbers_list[index])

            t_index= index +1
            while t_index < list_count:
                recursive_backtracking(t_index)

                t_index = t_index +1
                while t_index < list_count and numbers_list[t_index -1] == numbers_list[t_index]:
                    t_index = t_index +1

            final_list.append(current_list[:])
            current_list.pop()

        index = 0
        while index < list_count:
            recursive_backtracking(index)

            index = index +1
            while index < list_count and numbers_list[index -1] == numbers_list[index]:
                index = index +1

        final_list.append([])
        return final_list
        