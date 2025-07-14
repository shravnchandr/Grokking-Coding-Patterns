class Solution:
    def checkValidString(self, string: str) -> bool:
        bracket_stack, star_stack = list(), list()

        for index,char in enumerate(string):
            
            if char == '*':
                star_stack.append(index)
            elif char == '(':
                bracket_stack.append(index)

            else:
                if bracket_stack:
                    bracket_stack.pop()
                elif star_stack:
                    star_stack.pop()
                else:
                    return False
                
        while bracket_stack:
            if star_stack and bracket_stack[-1] < star_stack[-1]:
                bracket_stack.pop()
                star_stack.pop()
            
            else:
                return False
            
        return True
    