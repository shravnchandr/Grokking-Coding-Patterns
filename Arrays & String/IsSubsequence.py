class Solution:
    def isSubsequence(self, sub_string: str, string: str) -> bool:
        sub_index = 0

        for index, char in enumerate(string):
            if sub_index < len(sub_string) and sub_string[sub_index] == char:
                sub_index = sub_index +1

        return sub_index == len(sub_string)
        