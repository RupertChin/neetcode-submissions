from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Approach:
        sliding window and frequency map
        - count frequency of letters in s1
        - sliding window in s2, keep track of frequency of letters
            - if match return true
        """
        if len(s2) < len(s1):
            return False

        freq1 = defaultdict(int)
        freq2 = defaultdict(int)

        for char in s1:
            freq1[char] += 1
        
        l = 0
        r = 0
        while r < len(s1):
            freq2[s2[r]] += 1
            r += 1
        if freq1 == freq2:
            return True
        
        while r < len(s2):
            freq2[s2[r]] += 1
            freq2[s2[l]] -= 1
            if (freq2[s2[l]]) == 0:
                del freq2[s2[l]]
            r += 1
            l += 1

            if freq1 == freq2:
                return True
            
        
        return False
