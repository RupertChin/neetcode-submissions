class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Approach: 
        - same as regular house robber
        - instead manually pass max ind
            - start from 0, max is len(nums) - 2
            - start from 1, max is len(num) - 1
        
        problem:
        - edge case: 1 or 2 houses
        """

        def _rob(i: int, max_ind: int, robbed: list[int]) -> int:
            nonlocal nums
            if i > max_ind:
                return 0
            if robbed[i] != -1:
                return robbed[i]
            
            robbed[i] = max(_rob(i+1, max_ind, robbed), _rob(i+2, max_ind, robbed) + nums[i])
            return robbed[i]
        
        if len(nums) == 1:
            return nums[0]
        return max(_rob(0, len(nums)-2, [-1] * len(nums)), _rob(1, len(nums)-1, [-1] * len(nums)))
