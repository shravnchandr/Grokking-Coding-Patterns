from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combine_sum_list = list()

        def recursive_backtracking(index: int, current_list: List[int], current_sum: int) -> None:
            if current_sum == target:
                combine_sum_list.append(current_list[:])
                return
            
            while index < len(candidates):
                current_list.append(candidates[index])
                current_sum = current_sum + candidates[index]
                
                if current_sum <= target:
                    recursive_backtracking(index, current_list, current_sum)

                current_list.pop()
                current_sum = current_sum - candidates[index]

                index = index +1

        recursive_backtracking(0, [], 0)
        return combine_sum_list
    
