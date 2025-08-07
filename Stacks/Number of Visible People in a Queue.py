from collections import deque
from typing import List


class Solution:
    def searchInsert(self, numbers_list: List[int], target: int) -> int:
        left_index, right_index = 0, len(numbers_list) -1
        while left_index <= right_index:
            middle_index = (left_index + right_index) // 2

            if numbers_list[middle_index] < target:
                left_index = middle_index +1
            elif numbers_list[middle_index] > target:
                right_index = middle_index -1
            else:
                return middle_index

        return left_index

    def canSeePersonsCount(self, heights_list: List[int]) -> List[int]:
        final_list = [0]
        heights_queue = deque([heights_list[-1]])

        for index in range(len(heights_list) -2, -1, -1):
            height = heights_list[index]

            if height > heights_queue[-1]:
                final_list.append(len(heights_queue))
            else: 
                see_count = self.searchInsert(heights_queue, height)
                final_list.append(see_count +1)

            while heights_queue and heights_queue[0] < height:
                heights_queue.popleft()
            heights_queue.appendleft(height)

        return final_list[::-1]


    def canSeePersonsCount(self, heights_list: List[int]) -> List[int]:
        final_list = [0] * len(heights_list)

        heights_stack = []
        for index in range(len(heights_list) -1, -1, -1):
            height = heights_list[index]

            see_count = 0
            while heights_stack and heights_stack[-1] < height:
                heights_stack.pop()
                see_count = see_count +1

            if heights_stack:
                see_count = see_count +1

            final_list[index] = see_count
            heights_stack.append(height)

        return final_list
    