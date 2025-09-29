from typing import List


class Solution:
    def removeInvalidParentheses(self, string: str) -> List[str]:
        final_list, current_list = set(), []
        max_length = 0
        
        def recursive_function(index: int, open_count: int, close_count: int) -> None:
            nonlocal final_list, max_length

            if open_count == close_count:
                current_string = ''.join(current_list)
                current_length = len(current_string)

                if current_length > max_length:
                    final_list = {current_string}
                    max_length = current_length
                elif current_length == max_length:
                    final_list.add(current_string)

            while index < len(string):
                char = string[index]
                

                if char == '(':
                    current_list.append(char)
                    recursive_function(index +1, open_count +1, close_count)
                    current_list.pop()

                elif char == ')':
                    if close_count < open_count:
                        current_list.append(char)
                        recursive_function(index +1, open_count, close_count +1)
                        current_list.pop()
                    
                    else:

                        recursive_function(index +1, open_count, close_count)

                else:
                    current_list.append(char)
                    recursive_function(index +1, open_count, close_count)
                    current_list.pop()

                index = index +1


        recursive_function(0, 0, 0)
        return list(final_list)
        



from typing import List

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        res = set()

        # Step 1: count misplaced parentheses
        left_remove = right_remove = 0
        for ch in s:
            if ch == '(':
                left_remove += 1
            elif ch == ')':
                if left_remove > 0:
                    left_remove -= 1
                else:
                    right_remove += 1

        def dfs(index: int, left_count: int, right_count: int,
                left_rem: int, right_rem: int, path: list[str]) -> None:
            
            # End of string
            if index == len(s):
                if left_rem == 0 and right_rem == 0:
                    res.add("".join(path))
                return

            ch = s[index]

            # Option 1: remove char if it's parenthesis
            if ch == '(' and left_rem > 0:
                dfs(index + 1, left_count, right_count,
                    left_rem - 1, right_rem, path)
            elif ch == ')' and right_rem > 0:
                dfs(index + 1, left_count, right_count,
                    left_rem, right_rem - 1, path)

            # Option 2: keep char
            path.append(ch)
            if ch not in "()":
                dfs(index + 1, left_count, right_count,
                    left_rem, right_rem, path)
            elif ch == '(':
                dfs(index + 1, left_count + 1, right_count,
                    left_rem, right_rem, path)
            elif ch == ')' and right_count < left_count:
                dfs(index + 1, left_count, right_count + 1,
                    left_rem, right_rem, path)
            path.pop()

        dfs(0, 0, 0, left_remove, right_remove, [])
        return list(res)
