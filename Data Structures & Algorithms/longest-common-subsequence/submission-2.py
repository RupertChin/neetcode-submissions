class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        Approach:
        for each char, you can either include or exclude
        since can remove any chars to form subseq, is 2d dp problem using index of cur char per string
        """

        mem = [[0] * len(text2) for _ in range(len(text1))]

        def _dp(i: int, j: int) -> int:
            nonlocal mem, text1, text2
            if i >= len(text1) or j >= len(text2):
                return 0
            if mem[i][j] != 0:
                return mem[i][j]
            
            # 3 possible combinations
            cur_match = int(text1[i] == text2[j])
            mem[i][j] = max(mem[i][j], _dp(i+1, j+1)+cur_match)
            mem[i][j] = max(mem[i][j], _dp(i+1, j))
            mem[i][j] = max(mem[i][j], _dp(i, j+1))

            return mem[i][j]
        
        return _dp(0, 0)