class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sets = []
        def make_subsets(i: int, cur_set: List[int]):
            if i >= len(nums):
                sets.append(cur_set.copy())
                return
            make_subsets(i+1, cur_set)
            cur_set.append(nums[i])
            make_subsets(i+1,cur_set)
            cur_set.pop()
        
        make_subsets(0, [])
        return sets
