from typing import List


class Solution:
    def dailyTemperatures(self, temperatures_list: List[int]) -> List[int]:
        temperature_stack, index_stack = list(), list()
        warmer_days = [0] * len(temperatures_list)

        for index, temperature in enumerate(temperatures_list):
            
            while temperature_stack and temperature_stack[-1] < temperature:
                _, old_index = temperature_stack.pop(), index_stack.pop()
                warmer_days[old_index] = index - old_index

            temperature_stack.append(temperature)
            index_stack.append(index)

        return warmer_days
    