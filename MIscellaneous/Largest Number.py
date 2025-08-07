from collections import defaultdict
from typing import List


class Solution:
    def largestNumber(self, numbers_list: List[int]) -> str:
        
        numbers_list = [str(number) for number in numbers_list]
        numbers_list = sorted(numbers_list, reverse=True)

        numbers_dict = defaultdict(list)
        for number in numbers_list:
            numbers_dict[number[0]].append(number)

        final_list = []

        # for index in range(9, 0, -1):
        #     if str(index in numbers_dict):



        return ''.join(numbers_list)
        