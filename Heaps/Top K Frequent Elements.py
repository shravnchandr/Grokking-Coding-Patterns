from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, numbers_list: List[int], k_index: int) -> List[int]:
        numbers_count = Counter(numbers_list)
        
        count_buckets = [None] * (len(numbers_list) +1)
        for number,count in numbers_count.items():
            if count_buckets[count]:
                count_buckets[count].append(number)
            else:
                count_buckets[count] = [number]

        frequent_elements = list()
        for index in range(len(numbers_list), -1, -1):
            if count_buckets[index]:
                frequent_elements.extend(count_buckets[index])

            if len(frequent_elements) == k_index:
                break

        return frequent_elements
