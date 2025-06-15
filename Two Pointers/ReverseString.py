from typing import List


class Solution:
    def reverseString(self, string_list: List[str]) -> None:
        left_index, right_index = 0, len(string_list) -1

        while left_index < right_index:
            string_list[left_index], string_list[right_index] = string_list[right_index], string_list[left_index]
            left_index, right_index = left_index +1, right_index -1