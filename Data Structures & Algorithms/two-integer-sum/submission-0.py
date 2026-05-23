class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hashmap, key is num, value is index
        seen = {}
        for i, num in enumerate(nums):
            if target - num in seen:
                return [seen[target - num], i]
            else:
                seen[num] = i