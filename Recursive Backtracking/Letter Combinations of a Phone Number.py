from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        num_to_alpha = {
            '1': '', '2': 'abc', '3': 'def',
            '4': 'ghi', '5': 'jkl', '6': 'mno',
            '7': 'pqrs', '8': 'tuv', '9': 'wxyz',
        }

        letter_combo_list = list()

        def helperFunction(index: int, current_string: List[str]) -> None:
            if index == len(digits):
                letter_combo_list.append(''.join(current_string))
                return

            for char in num_to_alpha[digits[index]]:
                current_string.append(char)
                helperFunction(index +1, current_string)
                current_string.pop()

        helperFunction(0, [])
        return letter_combo_list
    