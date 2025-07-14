from typing import List


class Solution:
    def insert(self, intervals_list: List[List[int]], new_interval: List[int]) -> List[List[int]]:
        return_list = list()
        insert_flag = True

        if intervals_list and new_interval[1] < intervals_list[0][0]:
            return_list.append(new_interval)
            insert_flag = False

        def check_overlap(index: int) -> bool:
            old_start, old_end = intervals_list[index]
            new_start, new_end = new_interval

            return old_start <= new_end and new_start <= old_end
        
        def check_fitting(index: int) -> bool:
            _, old_end_x = intervals_list[index -1]
            old_start_y, _ = intervals_list[index]
            new_start, new_end = new_interval

            return old_end_x <= new_start and new_end <= old_start_y

        left_index = 0
        while left_index < len(intervals_list):

            if insert_flag and check_overlap(left_index):
                new_start = min(intervals_list[left_index][0], new_interval[0])

                right_index = left_index +1
                while right_index < len(intervals_list) and check_overlap(right_index):
                    right_index = right_index +1

                right_index = right_index -1
                new_end = max(intervals_list[right_index][1], new_interval[1])

                return_list.append([new_start, new_end])
                left_index = right_index

                insert_flag = False

            elif insert_flag and left_index > 0 and check_fitting(left_index):
                return_list.append(new_interval)
                return_list.append(intervals_list[left_index])
                insert_flag = False

            else:
                return_list.append(intervals_list[left_index])

            left_index = left_index +1

        if insert_flag:
            return_list.append(new_interval)

        return return_list


    def insert(self, intervals_list: List[List[int]], new_interval: List[int]) -> List[List[int]]:
        list_length = len(intervals_list)
        merged_intervals = []

        index = 0
        while index < list_length and intervals_list[index][1] < new_interval[0]:
            merged_intervals.append(intervals_list[index])
            index = index +1

        while index < list_length and intervals_list[index][0] <= new_interval[1]:
            new_interval[0] = min(new_interval[0], intervals_list[index][0])
            new_interval[1] = max(new_interval[1], intervals_list[index][1])
            index = index +1
        merged_intervals.append(new_interval)

        while index < list_length:
            merged_intervals.append(intervals_list[index])
            index = index +1

        return merged_intervals

