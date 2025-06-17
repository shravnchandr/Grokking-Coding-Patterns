import heapq
from typing import List


class Solution:
    def findKthLargest(self, numbers_list: List[int], k_index: int) -> int:
        numbers_list = [-number for number in numbers_list]
        heapq.heapify(numbers_list)

        for _ in range(k_index -1):
            heapq.heappop(numbers_list)
            
        return -heapq.heappop(numbers_list)
    

    def findKthLargest(self, numbers_list: List[int], k_index: int) -> int:
        numbers_heap = list()
        heapq.heapify(numbers_list)

        for number in numbers_list:
            heapq.heappush(numbers_heap, number)

            if len(numbers_heap) > k_index:
                heapq.heappop(numbers_heap)
            
        return heapq.heappop(numbers_heap)
    
        