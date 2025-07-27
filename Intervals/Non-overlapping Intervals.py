from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals_list: List[List[int]]) -> int:
        intervals_list = sorted(intervals_list, key=lambda pair: pair[1])

        previous_end = intervals_list[0][1]
        total_removed, index = 0, 1
        
        for index in range(1, len(intervals_list)):
            current_start, current_end = intervals_list[index][0], intervals_list[index][1]

            if current_start >= previous_end:
                previous_end = current_end
            else:
                total_removed = total_removed +1

        return total_removed
