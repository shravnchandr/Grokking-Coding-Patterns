class Solution:
    def longestPalindrome(self, string: str) -> str:
        longest_string = ''

        def find_palindrome(left_index: int, right_index: int) -> str:
            while left_index >= 0 and right_index < len(string) and string[left_index] == string[right_index]:
                left_index, right_index = left_index -1, right_index +1

            return string[left_index +1: right_index]

        for index in range(len(string)):
            even_string = find_palindrome(index, index +1)
            odd_string = find_palindrome(index, index)

            longest_string = max([even_string, odd_string, longest_string], key=lambda x: len(x))
            
        return longest_string

