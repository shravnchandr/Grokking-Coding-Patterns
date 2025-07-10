from typing import List


class Solution:
    def canJump(self, numbers_list: List[int]) -> bool:
        goal = len(numbers_list) -1

        for index in range(len(numbers_list) -2, -1, -1):
            if index + numbers_list[index] >= goal:
                goal = index

        return goal == 0
