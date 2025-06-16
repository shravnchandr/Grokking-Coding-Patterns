class Solution:
    def lengthOfLongestSubstring(self, string: str) -> int:
        max_length, unique_chars = 0, set()
        left_index, right_index = 0, 0

        while right_index < len(string):
            char = string[right_index]

            if char in unique_chars:
                max_length = max(right_index - left_index, max_length)

                while left_index < right_index and string[left_index] != char:
                    unique_chars.remove(string[left_index])
                    left_index = left_index +1

                # unique_chars.remove(char)
                left_index = left_index +1

            # else:
            #     unique_chars.add(char)

            unique_chars.add(char)
            right_index = right_index +1

        max_length = max(right_index - left_index, max_length)
        return max_length
