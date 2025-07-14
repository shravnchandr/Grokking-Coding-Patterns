from typing import List


class Solution:
    def plusOne(self, digits_list: List[int]) -> List[int]:
        digit_plus_one = digits_list[-1] +1
        carry = digit_plus_one // 10

        digits_list[-1] = digit_plus_one % 10
        
        index = len(digits_list) -2
        while index >= 0 and carry == 1:
            digit_plus_one = digits_list[index] +1
            carry = digit_plus_one // 10

            digits_list[index] = digit_plus_one % 10

        return digits_list
        