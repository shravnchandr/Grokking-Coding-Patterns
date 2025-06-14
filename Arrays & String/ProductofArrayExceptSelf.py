from typing import List


class Solution:
    def productExceptSelf(self, numbers_list: List[int]) -> List[int]:
        zero_count, list_product = 0, 1
        for number in numbers_list:
            if number == 0:
                zero_count = zero_count +1
            else:
                list_product = list_product * number
        
        if zero_count == 0:
            return [list_product // number for number in numbers_list]
        elif zero_count == 1:
            return [list_product if number == 0 else 0 for number in numbers_list]
        else:
            return [0 for _ in range(numbers_list)]

        