class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False
        s_counts = [0 for _ in range(0, 26)]
        t_counts = [0 for _ in range(0, 26)]
        for i in range(0, len(s)):
            s_counts[ord(s[i]) - ord('a')] += 1
            t_counts[ord(t[i]) - ord('a')] += 1
        
        for i in range(0, 26):
            if s_counts[i] != t_counts[i]:
                return False

        return True
