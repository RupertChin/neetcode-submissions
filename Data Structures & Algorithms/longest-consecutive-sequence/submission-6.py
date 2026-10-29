class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)

        max_len = 0
        while len(nums) > 0:
            cur_len = 1
            l = nums.pop()
            r = l
            while l - 1 in nums:
                cur_len += 1
                nums.remove(l - 1)
                l -= 1
            while r + 1 in nums:
                cur_len += 1
                nums.remove(r + 1)
                r += 1
            
            max_len = max(max_len, cur_len)
        
        return max_len
