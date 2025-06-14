from typing import List


class Solution:
    def generateParenthesis(self, number: int) -> List[str]:
        parentheses_list = list()
        current_parentheses = list()

        def backtrack(open_count, close_count):
            if open_count == close_count == number:
                parentheses_list.append(''.join(current_parentheses))
                return
            
            if open_count < number:
                current_parentheses.append('(')
                backtrack(open_count +1, close_count)
                current_parentheses.pop()

            if close_count < open_count:
                current_parentheses.append(')')
                backtrack(open_count, close_count +1)
                current_parentheses.pop()

        backtrack(0, 0)
        return parentheses_list

        