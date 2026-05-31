class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Approach:
        - 
        """

        r_max = [0] * len(height)
        cur_r_max = 0
        # backwards pass first, store r_max per i
        for i, num in reversed(list(enumerate(height))):
            cur_r_max = max(cur_r_max, num)
            r_max[i] = cur_r_max
        
        res = 0
        cur_l_max = 0
        for i, num in enumerate(height):
            cur = min(cur_l_max, r_max[i]) - num
            if cur > 0:
                res += cur
            cur_l_max = max(cur_l_max, num)
        
        return res