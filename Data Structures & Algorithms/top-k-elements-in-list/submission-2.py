from collections import defaultdict
from heapq import heappush, heappop

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        pq = []
        for num in nums:
            counts[num] += 1
        for key, value in counts.items():
            heappush(pq, (value, key))
            if len(pq) > k:
                heappop(pq)

        res = []
        for i in range(k):
            res.append(heappop(pq)[1])
        return res

"""
Notes for self:
- initial try was max heap, worked but slightly slower than min heap
- second try was min heap, same asymptotic runtime but never stores more than k elements, faster
- note: heapq is faster for most heap functions, but isn't thread safe. only use PriorityQueue when multithreaded
"""
        