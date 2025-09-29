class Solution:
    def calculate(self, string: str) -> int:
        string = string.replace(' ', '')
        digits_stack, operator_stack = [], []

        brackets_dict, brackets_stack = {}, []
        for index,char in enumerate(string):
            if char == '(':
                brackets_stack.append(index)
            if char == ')':
                brackets_dict[brackets_stack.pop()] = index

        index = 0
        while index < len(string):
            char = string[index]

            if char == '(':
                start_index = index +1
                end_index = brackets_dict[index]
                index = end_index +1

                answer = self.calculate(string[start_index: end_index])
                if operator_stack and operator_stack[-1] == '-':
                    operator_stack.pop()
                    answer = -answer

                digits_stack.append(answer)

            elif char.isdigit():

                digit_string = 0
                while index < len(string) and string[index].isdigit():
                    digit_string = (digit_string * 10) + int(string[index])
                    index = index +1

                if operator_stack and operator_stack[-1] == '-':
                    operator_stack.pop()
                    digit_string = -digit_string

                digits_stack.append(digit_string)

            else:
                operator_stack.append(char)
                index = index +1
        
        return sum(digits_stack)

    def calculate(self, string: str) -> int:
        memory_stack = []
        result, operand, sign = 0, 0, 1

        for char in string:
            if char.isdigit():
                operand = (operand * 10) + int(char)
            
            elif char == '+':
                result = result + (sign * operand)
                operand, sign = 0, 1
            elif char == '-':
                result = result + (sign * operand)
                operand, sign = 0, -1

            elif char == '(':
                memory_stack.append(result)
                memory_stack.append(sign)

                result, sign = 0, 1
            elif char == ')':
                result = result + (sign * operand)
                result = result * memory_stack.pop()
                result = result + memory_stack.pop()

                operand = 0

        return result + (sign * operand)

