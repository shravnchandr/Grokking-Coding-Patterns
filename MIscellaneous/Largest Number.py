import functools
from typing import List


class Solution:
    def largestNumber(self, numbers_list: List[int]) -> str:
        numbers_list = list(map(str, numbers_list))

        def compare(x, y):
            if x + y > y + x:
                return -1  # x should be placed before y
            elif x + y < y + x:
                return 1   # y should be placed before x
            else:
                return 0
            
        numbers_list.sort(key=functools.cmp_to_key(compare))
        final_string = ''.join(numbers_list)

        return final_string if final_string[0] != '0' else '0'
    