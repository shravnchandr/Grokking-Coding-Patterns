from collections import defaultdict
from typing import List


class Solution:
    def partitionLabels(self, string: str) -> List[int]:
        char_indicies = defaultdict(list)
        for index,char in enumerate(string):
            char_indicies[char].append(index)

        return_list = list()
        left_index = 0
        while left_index < len(string):
            char = string[left_index]

            max_index = char_indicies[string[left_index]][-1] +1
            right_index = left_index +1

            while right_index < max_index:
                max_index = max(max_index, char_indicies[string[right_index]][-1] +1)
                right_index = right_index +1

            return_list.append(right_index - left_index)
            left_index = right_index

        return return_list
        