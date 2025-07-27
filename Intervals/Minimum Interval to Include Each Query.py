from typing import List


class Solution:
    def minInterval(self, intervals_list: List[List[int]], queries_list: List[int]) -> List[int]:
        intervals_list = sorted(intervals_list, key=lambda x: x[1] - x[0] +1)

        return_list = []
        for query in queries_list:
            query_flag = True

            for start,end in intervals_list:
                if start <= query <= end:
                    query_flag = False
                    return_list.append(end - start +1)
                    break

            if query_flag:
                return_list.append(-1)

        return return_list
    
        
    def minInterval(self, intervals_list: List[List[int]], queries_list: List[int]) -> List[int]:
        intervals_list = sorted(intervals_list) #, key= lambda pair: pair[1])

        dp_memoization = {}
        def find_interval(query:int, left_index: int, right_index: int) -> int:
            if right_index < left_index:
                return float('inf')

            if not intervals_list[left_index][0] <= query <= intervals_list[right_index][1]:
                return float('inf')

            if (query, left_index, right_index) in dp_memoization:
                return dp_memoization[(query, left_index, right_index)]    
            
            middle_index = (left_index + right_index) // 2
            start, end = intervals_list[middle_index]

            if start <= query <= end:
                check_left_area = find_interval(query, left_index, middle_index -1)
                check_right_area = find_interval(query, middle_index +1, right_index)

                min_interval = min(check_left_area, check_right_area, end - start +1)

            else:
                check_left_area = find_interval(query, left_index, middle_index -1)
                check_right_area = find_interval(query, middle_index +1, right_index)

                min_interval = min(check_left_area, check_right_area)

            dp_memoization[(query, left_index, right_index)] = min_interval
            return dp_memoization[(query, left_index, right_index)]

        return_list = []
        for query in queries_list:
            dp_memoization = {}

            interval_size = find_interval(query, 0, len(intervals_list) -1)
            interval_size = interval_size if interval_size != float('inf') else -1
            
            return_list.append(interval_size)

        return return_list
    