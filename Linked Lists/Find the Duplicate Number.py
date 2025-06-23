from typing import List


class Solution:
    def findDuplicate(self, numbers_list: List[int]) -> int:
        hare_index, tortoise_index = numbers_list[0], numbers_list[0]

        while True:
            hare_index = numbers_list[numbers_list[hare_index]]
            tortoise_index = numbers_list[tortoise_index]

            if hare_index == tortoise_index:
                break

        tortoise_index = numbers_list[0]
        while hare_index != tortoise_index:
            hare_index = numbers_list[hare_index]
            tortoise_index = numbers_list[tortoise_index]

        return tortoise_index
    