from typing import List


class Solution:
    def twoSum(self, numbers_list: List[int], target_sum: int) -> List[int]:
        difference_dict = dict()

        for index, number in enumerate(numbers_list):
            if number in difference_dict:
                return [index ,difference_dict[number]]
            
            difference_dict[target_sum - number] = index