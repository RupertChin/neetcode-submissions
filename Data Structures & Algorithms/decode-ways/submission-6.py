class Solution:
    def numDecodings(self, s: str) -> int:
        """
        Approach:
        - dp, at each index take either 1 or 2 digits
        - if the starting digit is not between 1 - 9 then no
        - if the starting digit is not 1 or 2 then 

        Approach 2:
        - bottom up dp
        """

        max_decodings = [0] * (len(s) + 1)
        max_decodings[-1] = 1
        for i in range(len(s)-1, -1, -1):
            if s[i] == '0':
                continue

            # take current digit
            max_decodings[i] = max_decodings[i+1]
            
            # take current and next digit if valid
            if i < len(s)-1 and int(s[i:i+2]) <= 26:
                # max_decodings[i] = max(max_decodings[i], max_decodings[i+2], max_decodings[i] + max_decodings[i+2])
                max_decodings[i] += max_decodings[i+2]

        return max_decodings[0]
            
            
            


