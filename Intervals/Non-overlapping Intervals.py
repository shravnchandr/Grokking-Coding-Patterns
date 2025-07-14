from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals_list: List[List[int]]) -> int:
        intervals_list = sorted(intervals_list, key=lambda x:x[0])

        def check_overlap(old_index: int, new_index: int) -> bool:
            old_start, old_end = intervals_list[old_index]
            new_start, new_end = intervals_list[new_index]

            return old_start <= new_end and new_start <= old_end

        previous_end = intervals_list[0][1]
        total_removed, index = 0, 1
        
        while index < len(intervals_list):
            if check_overlap(index -1, index):
                previous_end = min(previous_end, intervals_list[index][1])
                total_removed = total_removed +1
            
            else:
                previous_end = intervals_list[index][1]

            index = index +1

        return total_removed
