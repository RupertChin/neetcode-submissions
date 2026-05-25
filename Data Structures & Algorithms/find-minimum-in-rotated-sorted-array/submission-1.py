class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        """
        Approach 2: 
        - check r l mid:
            - l < mid < r, minimum is at l?
            - r < mid, rotated, minimum is on right side, l = mid + 1
            - l > mid, rotated, minimum is middle or left side, r = mid
        """
        while l < r:
            mid = (l + r) // 2
            print(f"{l}, {r}, {mid}")

            # if nums[l] < nums[mid] and nums[mid] < nums[r]: 
            #     return l
            if nums[r] < nums[mid]:
                l = mid + 1
            elif nums[l] > nums[mid]: # l > mid
                r = mid
            else:
                return nums[l]

        return nums[r]

