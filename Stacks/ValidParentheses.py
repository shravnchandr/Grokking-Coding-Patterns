class Solution:
    def isValid(self, string: str) -> bool:
        parentheses_map = {'}':'{', ')':'(', ']':'['}
        parentheses_stack = list()

        for parentheses in string:
            if parentheses in parentheses_map.values():
                parentheses_stack.append(parentheses)

            else:
                if not parentheses_stack or parentheses_stack.pop() != parentheses_map[parentheses]:
                    return False
                
        return True if not parentheses_stack else False