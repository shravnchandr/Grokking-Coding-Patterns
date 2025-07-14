from typing import List


class Solution:
    def merge(self, intervals_list: List[List[int]]) -> List[List[int]]:
        intervals_list = sorted(intervals_list, key=lambda x: x[0])
        merged_list = [intervals_list[0]]

        intervals_index, merged_index = 1, 0
        while intervals_index < len(intervals_list):
            interval, merge = intervals_list[intervals_index], merged_list[merged_index]

            if interval[0] <= merge[1] <= interval[1]:
                merged_list[merged_index] = [merge[0], interval[1]]

            elif merge[0] <= interval[0] <= interval[1] <= merge[1]:
                merged_list[merged_index] = merge

            else:
                merged_list.append(interval)
                merged_index = merged_index +1

            intervals_index = intervals_index +1

        return merged_list

            
