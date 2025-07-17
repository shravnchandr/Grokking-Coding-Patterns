from typing import Tuple


class Solution:
    def countSubstrings(self, string: str) -> int:
        final_count = 0

        def find_palindrome(left_index: int, right_index: int) -> Tuple[int]:
            palindrome_count = 0

            while left_index >= 0 and right_index < len(string) and string[left_index] == string[right_index]:
                palindrome_count = palindrome_count +1
                left_index, right_index = left_index -1, right_index +1

            return palindrome_count

        palindrome_indicies = set()

        for index in range(len(string)):
            even_count = find_palindrome(index, index +1)
            odd_count = find_palindrome(index, index)

            final_count = final_count + even_count + odd_count

        return final_count

