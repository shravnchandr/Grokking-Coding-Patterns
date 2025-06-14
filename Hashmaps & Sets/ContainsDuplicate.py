from typing import List


class Solution:
    def containsDuplicate(self, numbers_list: List[int]) -> bool:
        numbers_set = set()

        for number in numbers_list:
            if number in numbers_set:
                return True
            
            numbers_set.add(number)

        return False