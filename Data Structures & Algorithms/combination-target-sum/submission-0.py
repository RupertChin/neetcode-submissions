class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        Approach:
        for each number in nums:
        - add as many of that number as possible to running combination
            - for each possible number of that num (including 0), recursively call on next num in nums
        """
        combinations = []
        cur_nums = []
        # is there a way to store partially computed combinations?

        def buildCombinations(nums_ind: int, cur_sum: int) -> None:
            nonlocal nums, target, combinations, cur_nums

            if nums_ind >= len(nums):
                return

            num_added = 0 # track how many of current num added to sum
            while cur_sum < target:
                buildCombinations(nums_ind+1, cur_sum)

                cur_nums.append(nums[nums_ind])
                cur_sum += nums[nums_ind]
                num_added += 1

                if cur_sum == target:
                    combinations.append(cur_nums.copy())
            
            del cur_nums[-num_added:]
            cur_sum -= num_added * nums[nums_ind]

            return
        
        buildCombinations(0, 0)
        return combinations

