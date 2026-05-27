class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Approach, backwards dp
        """
        if (n <= 2):
            return n # edge case

        # dp = [0] * n
        ahead_2 = 1
        ahead_1 = 2

        curr = 0
        for i in range(n-3, -1, -1):
            curr = ahead_2 + ahead_1
            ahead_2 = ahead_1
            ahead_1 = curr

        return curr