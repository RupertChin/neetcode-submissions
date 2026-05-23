from collections import defaultdict
from heapq import heappush, heappop

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        pq = []
        for num in nums:
            counts[num] += 1
        for key, value in counts.items():
            heappush(pq, (value*-1, key)) # to make max heap

        res = []
        for _ in range(k):
            res.append(heappop(pq)[1])

        return res
        