from collections import Counter
from typing import List


class Solution:
    def majorityElement(self, numbers_list: List[int]) -> int:
        number_counter = Counter(numbers_list)
        
        max_element, max_count = numbers_list[0], 0
        for number, count in number_counter.items():
            if count > max_count:
                max_element, max_count = number, count

        # return max_element
        
        max_element, max_count = numbers_list[0], 0
        for number in numbers_list:
            if max_count == 0:
                max_element = number

            max_count = max_count +1 if number == max_element else max_count -1

        return max_element
