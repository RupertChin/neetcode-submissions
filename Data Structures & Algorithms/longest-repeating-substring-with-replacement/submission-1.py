from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = defaultdict(int)

        """
        Approach:
        - frequency dict, remove kv pairs when v = 0
        - l and r sliding window
        - track num pairs, ensure always below k, move l when above
        - track substr length
        """

        l = 0
        r = 0
        max_substr_len = 0
        while r < len(s):
            seen[s[r]] += 1

            """
            if more than 1 letter, check if less than k subs needed
            if not, increment l until: 
                - num unique characters <= 2
                - either char count <= k
            2 while loops?
            """
            if len(seen.keys()) > 1:                
                while len(seen.keys()) > 1:
                    """
                    if sum of values, keep incrementing l
                    """
                    num_replacements =  r - l + 1 - max(seen.values())
                    if num_replacements <= k:
                        break
                    
                    seen[s[l]] -= 1
                    if seen[s[l]] == 0:
                        del seen[s[l]]
                    l += 1

            max_substr_len = max(max_substr_len, r - l + 1)
            r += 1
        
        return max_substr_len
