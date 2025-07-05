import heapq
from typing import List


class KthLargest:

    def __init__(self, k_index: int, numbers_list: List[int]):
        self.numbers_list = [-number for number in numbers_list]
        self.k_index = k_index

        heapq.heapify(self.numbers_list)

    def add(self, val: int) -> int:
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)