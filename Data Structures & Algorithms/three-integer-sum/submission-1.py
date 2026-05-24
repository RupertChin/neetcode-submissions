class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        triplets = set()
        for i in range(1, len(nums)-1):
            l = i - 1
            r = i + 1

            while (l >= 0 and r < len(nums)):
                total = nums[l] + nums[i] + nums[r]
                if (total == 0):
                    triplets.add((nums[l], nums[i], nums[r]))
                    l -= 1
                    r += 1
                elif (total > 0):
                    l -= 1
                elif (total < 0):
                    r += 1
            
        triplets = list(triplets)
        for triplet in triplets:
            triplet = list(triplet)
        
        return triplets