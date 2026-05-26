import heapq

class MedianFinder:
    """
    Approach:
    - maintain a sorted array
        - problem: insertion takes O(n) for not at the end
        - solution: use 2 heaps (max, min) instead, ensure sizes are no more than 1 apart
            - if >1 diff in size, mvoe elements to other heap
    - for each number inserted, use binary search to find its insertion location
    """
    max_heap: list # used for entries less than median
    min_heap: list # used for entries greater than median

    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        if len(self.min_heap) == 0:
            heapq.heappush(self.min_heap, num)
        elif num < self.min_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)
        
        if len(self.max_heap) - len(self.min_heap) > 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        elif len(self.min_heap) - len(self.max_heap) > 1: 
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def findMedian(self) -> float:
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        elif len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        else:
            return self.min_heap[0]
        