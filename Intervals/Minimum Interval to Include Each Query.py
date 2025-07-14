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
        intervals_list = sorted(intervals_list)

        return_list = []
        for query in queries_list:
            interval_size = float('inf')    

            left_index, right_index = 0, len(intervals_list)
            while left_index <= right_index:
                middle_index = (left_index + right_index) // 2
                start, end = intervals_list[middle_index]

                if start <= query <= end:
                    interval_size = min(interval_size, end - start +1)
                    right_index = middle_index -1

                else:
                    if query < start:
                        right_index = middle_index -1
                    elif query > end:
                        left_index = middle_index +1

            interval_size = interval_size if interval_size != float('inf') else -1
            return_list.append(interval_size)

        return return_list
    