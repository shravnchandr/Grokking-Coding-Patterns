from typing import List


class Solution:
    def subsetSum(self, numbers_list: List[int], target_sum: int) -> bool:
        total_sum = sum(numbers_list) + target_sum

        if total_sum %2 != 0 or total_sum < 0:
            return False
        
        target_sum = total_sum // 2

        dp_list = [0] * (target_sum +1)
        dp_list[0] = 1

        for number in numbers_list:
            for current_sum in range(target_sum, number -1, -1):

                dp_list[current_sum] = dp_list[current_sum] + dp_list[current_sum - number]

                if dp_list[target_sum] > 0:
                    return True

        return False
    

    def lastStoneWeightII(self, stones_weight: List[int]) -> int:
        if len(stones_weight) == 1:
            return stones_weight[0]

        for weight in range(sum(stones_weight)):
            if self.subsetSum(stones_weight, weight):
                return weight


        