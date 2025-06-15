from typing import List


class Solution:
    def findMedianSortedArrays(self, list_x: List[int], list_y: List[int]) -> float:
        if len(list_x) > len(list_y):
            list_x, list_y = list_y, list_x

        length_x, length_y = len(list_x), len(list_y)

        left_index, right_index = 0, length_x
        while left_index <= right_index:
            partition_x = (left_index + right_index) // 2
            partition_y = ((length_x + length_y +1) // 2) - partition_x

            max_left_x = float('-inf') if partition_x == 0 else list_x[partition_x -1]
            min_right_x = float('inf') if partition_x == length_x else list_x[partition_x]

            max_left_y = float('-inf') if partition_y == 0 else list_y[partition_y -1]
            min_right_y = float('inf') if partition_y == length_y else list_y[partition_y]

            if max_left_x <= min_right_y and max_left_y <= min_right_x:
                if (length_x + length_y) % 2 == 0:
                    return (max(max_left_x, max_left_y) + min(min_right_x, min_right_y)) / 2
                else:
                    return max(max_left_x, max_left_y)
                
            elif max_left_x > min_right_y:
                right_index = partition_x -1
            else:
                left_index = partition_x +1
            