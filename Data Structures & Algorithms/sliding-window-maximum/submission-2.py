

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        Keep a max heap of tuples ordered by the max first num, 
        then min second num
        """

        min_heap = []
        res = []

        for i, num in enumerate(nums):
            heapq.heappush(min_heap, (num*(-1), i))
            # print(min_heap)
            if i >= k-1:
                while min_heap[0][1] <= i-k:
                    heapq.heappop(min_heap)
                    # print(f"pop: {min_heap}")
                res.append(min_heap[0][0]*(-1))
        
        return res
                
        