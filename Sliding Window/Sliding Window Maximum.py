from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, numbers_list: List[int], window_size: int) -> List[int]:
        max_queue, window_max = deque(), list()

        for index, number in enumerate(numbers_list):
            while max_queue and index - window_size >= max_queue[0]:
                max_queue.popleft()

            while max_queue and numbers_list[max_queue[-1]] < number:
                max_queue.pop()

            max_queue.append(index)
        
            if index >= window_size -1:
                window_max.append(numbers_list[max_queue[0]])

        return window_max
    