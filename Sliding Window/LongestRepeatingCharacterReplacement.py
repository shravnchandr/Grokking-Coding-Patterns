from collections import defaultdict


class Solution:
    def characterReplacement(self, string: str, replace_count: int) -> int:
        max_length, char_count = 0, defaultdict(int)
        left_index, right_index = 0, 0

        while right_index < len(string):
            right_char = string[right_index]
            char_count[right_char] = char_count[right_char] +1

            current_length = right_index - left_index +1
            current_replace = current_length - max(char_count.values())

            while current_replace > replace_count:
                left_char = string[left_index]

                char_count[left_char] = char_count[left_char] -1
                left_index = left_index +1

                current_length = right_index - left_index +1
                current_replace = current_length - max(char_count.values())

            max_length = max(current_length, max_length)
            right_index = right_index +1

        max_length = max(right_index - left_index +1, max_length)
        return max_length
