class Solution:
    def rob(self, nums: List[int]) -> int:
        max_rob = [-1] * len(nums)

        def _rob(i: int) -> int:
            nonlocal nums, max_rob

            if i >= len(nums):
                return 0 
            if max_rob[i] != -1:
                return max_rob[i]
            
            max_rob[i] = max(_rob(i+1), _rob(i+2) + nums[i])
            return max_rob[i]
        
        return _rob(0)