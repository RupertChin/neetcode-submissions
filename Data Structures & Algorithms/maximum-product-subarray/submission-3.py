class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        Approach: 
        - iterate through nums, tracking max/running product
        - need to account for negatives... 
            - seperate tracker for if there's a negative?
        - maybe forwards dp tracking both the max and min?
        """

        max_prod = float("-inf")
        cur_high = 1
        cur_low = 1
        for num in nums:
            a = cur_high*num
            b = cur_low*num
            cur_high = max(a, b, num)
            cur_low = min(a, b, num)
            max_prod = max(max_prod, cur_high)

            if num == 0:
                cur_high = 1
                cur_low = 1
            # print(f"{max_prod}, ")
        return max_prod

