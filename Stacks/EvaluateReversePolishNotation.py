from typing import List


class Solution:
    def evalRPN(self, tokens_list: List[str]) -> int:
        eval_stack = list()

        for token in tokens_list:
            if token[-1].isalnum():
                eval_stack.append(int(token))
            else:
                number_right = eval_stack.pop()
                number_left = eval_stack.pop()
                
                eval_result = eval(f"{number_left} {token} {number_right}")
                eval_stack.append(int(eval_result))

        return eval_stack[0]
