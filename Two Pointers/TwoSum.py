from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = dict()

        for index,value in enumerate(nums):
            
            if value in hashMap.keys():
                return [hashMap[value], index]
            
            hashMap[target - value] = index
        