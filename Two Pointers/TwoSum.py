from typing import List

class Solution:
    def twoSum(self, numbers_list: List[int], target: int) -> List[int]:
        difference_dict = dict()

        for index,number in enumerate(numbers_list):
            
            if number in difference_dict.keys():
                return [difference_dict[number], index]
            
            difference_dict[target - number] = index
        