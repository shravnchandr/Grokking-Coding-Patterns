from typing import List


class Solution:
    def longestCommonPrefix(self, strings_list: List[str]) -> str:
        prefix_string = ""
        for index, char in enumerate(strings_list[0]):
            for string in strings_list:
                if index < len(string) and string[index] == char:
                    continue
                else:
                    return prefix_string
                
            prefix_string = prefix_string + char

        return prefix_string
