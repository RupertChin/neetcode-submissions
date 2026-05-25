class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Approach:
        binary search to find start of array, then re-binary search with new bounds to find value?
        check l, r, mid
        - if l > mid, start is somewhere mid to left side
        - if r < mid, start is somewhere on the right side
        - otherwise regular bounds are in use.
        """

        # find starting index
        l = 0
        r = len(nums) - 1
        start = -1
        while l < r:
            mid = (l + r) // 2

            if nums[l] > nums[mid]:
                r = mid
            elif nums[r] < nums[mid]:
                l = mid + 1
            else:
                start = l
                break
        if start == -1:
            start = r
        
        # now regular binary search with new bounds. map value to diff from start mod len
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            true_mid = (start + mid) % len(nums)
            if nums[true_mid] < target:
                l = mid + 1
            else:
                r = mid
        
        true_res = (start + r) % len(nums)
        if nums[true_res] == target:
            return true_res
        else:
            return -1
        