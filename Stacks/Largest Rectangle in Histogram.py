from typing import List


class Solution:
    def largestRectangleArea(self, heights_list: List[int]) -> int:
        heights_stack, max_area = list(), 0

        for index, height in enumerate(heights_list):
            stack_index = index

            while heights_stack and heights_stack[-1][1] > height:
                stack_index, stack_height = heights_stack.pop()

                current_area = stack_height * (index - stack_index)
                max_area = max(current_area, max_area)

            heights_stack.append((stack_index, height))

        while heights_stack:
            stack_index, stack_height = heights_stack.pop()

            current_area = stack_height * (len(heights_list) - stack_index)
            max_area = max(current_area, max_area)

        return max_area
