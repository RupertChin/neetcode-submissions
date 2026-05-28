class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        Approach:
        bottom up dp?
        - for each char going backwards, iterate forward
            - for every number > start, see longest subseq from that point
            - subseq[i] = max of all following indices storing nums > start
        """

        subseq = [1] * len(nums)

        # do stuff
        for i in range(len(nums)-1, -1, -1):
            max_substr = 1
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    max_substr = max(max_substr, subseq[j]+1)
            
            subseq[i] = max_substr

        print(subseq)
        return max(subseq)