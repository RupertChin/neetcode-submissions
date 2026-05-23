class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # calculate forward and backward pass running products
        cur_product = 1
        forward_products = [1] * len(nums)
        for i, num in enumerate(nums):
            cur_product *= num
            forward_products[i] = cur_product

        cur_product = 1
        backward_products = [1] * len(nums)
        for i in range(len(nums)-1, -1, -1):
            cur_product *= nums[i]
            backward_products[i] = cur_product

        # use to calculate final products
        res = [1] * len(nums)
        for i in range(len(nums)):
            res[i] = (forward_products[i-1] if i > 0 else 1) * (backward_products[i+1] if i < len(nums)-1 else 1)
        return res

"""
Note to self:
- future improvement: instead of precomputing prefix/suffix arrays, compute in place in the result
    - just keep the running product going both ways, multiply lol, saves a O(N) pass and reduces memory
"""
