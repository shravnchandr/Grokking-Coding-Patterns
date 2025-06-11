from typing import List


class Solution:
    def canPartition(self, numbers_list: List[int]) -> bool:
        if len(numbers_list) < 2 or sum(numbers_list) %2 != 0:
            return False

        numbers_list = sorted(numbers_list)

        left_index, right_index = 0, len(numbers_list) -1
        left_sum, right_sum = numbers_list[left_index], numbers_list[right_index]
        
        while left_index < right_index:
            
            if left_sum < right_sum:
                left_index = left_index +1
                left_sum = left_sum + numbers_list[left_index]

            elif left_sum > right_sum:
                right_index = right_index -1
                right_sum = right_sum + numbers_list[right_index]
            
            else:
                if left_index +1 == right_index:
                    return True
                else:
                    left_index = left_index +1
                    left_sum = left_sum + numbers_list[left_index]

        return left_sum == right_sum

