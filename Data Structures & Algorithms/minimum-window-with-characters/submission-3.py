from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        expected = defaultdict(int)
        seen = {}
        for c in t:
            seen[c] = 0
            expected[c] += 1

        
        l = 0
        r = 0
        min_substr_range = [-1, len(s)] # [l, r]
        while r < len(s):
            """
            approach: 
            - increment r until requirement satisfied
            - note down substr length
            - increment l until requirement not satisfied, noting len
            - continue increment l until it reaches a character in t
                - actually no need lol
            - repeat until r out of bounds
            """

            # increment r until requirement satisfied
            while r < len(s):
                if s[r] in seen.keys():
                    seen[s[r]] += 1

                is_valid_substr = True
                for c, count in seen.items():
                    if count < expected[c]:
                        is_valid_substr = False
                        break
                if is_valid_substr:
                    break

                r += 1
            
            if r >= len(s):
                break
            
            # note substr length if new min, then try to increment l
            while l <= r:
                is_valid_substr = True
                for c, count in seen.items():
                    if count < expected[c]:
                        is_valid_substr = False
                        break
                if not is_valid_substr:
                    break
                
                if r - l < min_substr_range[1] - min_substr_range[0]:
                    min_substr_range[0] = l
                    min_substr_range[1] = r
                
                # increment l here
                if s[l] in seen.keys():
                    seen[s[l]] -= 1
                l += 1
                

            r += 1
            # check if all values > 0

            # how to know when to increment l?
        
        if min_substr_range[1] - min_substr_range[0] > len(s):
            return ""
        else:
            return s[min_substr_range[0]:min_substr_range[1]+1]
            