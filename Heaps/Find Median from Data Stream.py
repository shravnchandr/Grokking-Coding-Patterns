import heapq


class MedianFinder:

    def __init__(self):
        self.max_heap = list()
        self.min_heap = list()

    def addNum(self, number: int) -> None:
        heapq.heappush(self.max_heap, -number)

        if self.min_heap and self.max_heap and self.min_heap[0] < -self.max_heap[0]:
            number = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, number)

        if len(self.max_heap) > len(self.min_heap) +1:
            number = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, number)
        elif len(self.min_heap) > len(self.max_heap):
            number = -heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, number)

    def findMedian(self) -> float:
        total_elements = len(self.max_heap) + len(self.min_heap)

        if total_elements % 2 == 1:
            if len(self.max_heap) > len(self.min_heap):
                return -self.max_heap[0]
            else:
                return self.min_heap[0]
        else:
            return (-self.max_heap[0] + self.min_heap[0]) / 2.0
