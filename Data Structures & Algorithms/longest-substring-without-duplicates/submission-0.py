from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = defaultdict(int)
        max_substr_len = 0

        """
        approach: sliding window with char counter
        increment r ptr until duplicate char found via frequency dict
        when duplicate found, increment l ptr until no more duplicate
        repeat until end, tracking max substr len
        """

        l = 0
        r = 0
        while r < len(s):
            # ensure valid substr
            while seen[s[r]] > 0:
                seen[s[l]] -= 1
                l += 1
            seen[s[r]] += 1

            max_substr_len = max(max_substr_len, r - l + 1)

            r += 1
        
        return max_substr_len

