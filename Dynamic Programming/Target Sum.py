from typing import List


class Solution:
    def findTargetSumWays(self, numbers_list: List[int], target_sum: int) -> int:
        total_sum = sum(numbers_list) + target_sum

        if total_sum %2 != 0 or total_sum < 0:
            return 0
        
        target_sum = total_sum // 2

        dp_list = [0] * (target_sum +1)
        dp_list[0] = 1

        for number in numbers_list:
            for current_sum in range(target_sum, number -1, -1):

                dp_list[current_sum] = dp_list[current_sum] + dp_list[current_sum - number]

        return dp_list[target_sum]
        