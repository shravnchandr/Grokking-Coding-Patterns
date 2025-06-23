from typing import List


class Solution:
    def longestConsecutive(self, numbers_list: List[int]) -> int:
        if not numbers_list:
            return 0
        
        numbers_set = set(numbers_list)
        consecutive_map, seen_numbers = dict(), set()

        for number in numbers_set:
            temp_number, temp_count = number -1, 1

            while temp_number in numbers_set and temp_number not in seen_numbers:
                seen_numbers.add(temp_number)
                temp_number, temp_count = temp_number -1, temp_count +1
            seen_numbers.add(number)

            consecutive_map[number] = consecutive_map.get(temp_number, 0) + temp_count 

        return max(consecutive_map.values())
