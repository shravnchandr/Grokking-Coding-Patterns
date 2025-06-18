from collections import defaultdict
from typing import List


class Solution:
    def lengthOfLIS(self, numbers_list: List[int]) -> int:
        seq_count = defaultdict(int)
        seq_count[numbers_list[-1]] = 1
        
        index = len(numbers_list) -2
        while index >= 0:
            number = numbers_list[index]

            greater_than = [value for key,value in seq_count.items() if key > number]
            if greater_than:
                seq_count[number] = max(greater_than) +1

            else:
                seq_count[number] = 1

            index = index -1

        return max(seq_count.values())

            
    def lengthOfLIS(self, numbers_list: List[int]) -> int:
        dp_storage = [1] * len(numbers_list)

        for right_index in range(len(numbers_list)):
            for left_index in range(right_index):

                if numbers_list[right_index] > numbers_list[left_index]:
                    dp_storage[right_index] = max(dp_storage[right_index], dp_storage[left_index] +1)

        return max(dp_storage)
