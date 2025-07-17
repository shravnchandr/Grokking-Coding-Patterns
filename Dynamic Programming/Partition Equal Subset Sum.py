from typing import List


class Solution:
    def canPartition(self, numbers_list: List[int]) -> bool:
        list_length, list_sum = len(numbers_list), sum(numbers_list)

        if list_length < 2 or list_sum %2 != 0:
            return False
        
        target_sum = list_sum // 2
        dp_array = [False] * (target_sum +1)
        dp_array[0] = True

        for number in numbers_list:
            for index in range(target_sum, number -1, -1):
                dp_array[index] = dp_array[index] or dp_array[index - number]

        return dp_array[target_sum]
    