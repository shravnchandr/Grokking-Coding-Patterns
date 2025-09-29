from typing import List


class Solution:
    def removeDuplicates(self, numbers_list: List[int]) -> int:
        left_index, right_index = 0, 1

        while right_index < len(numbers_list):
             