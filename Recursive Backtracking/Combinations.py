from typing import List


class Solution:
    def combine(self, number: int, length: int) -> List[List[int]]:
        combine_list = list()
        
        def recursive_backtracking(index: int, current_list: List[int]) -> None:
            if len(current_list) == length:
                combine_list.append(current_list[:])
                return
            
            for value in range(index, number +1):
                current_list.append(value)
                recursive_backtracking(value +1, current_list)
                current_list.pop()

        recursive_backtracking(1, [])
        return combine_list
