class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        Approach: 
        dp bottom up
        - store fewest num coins to arrive at end
        - at every step take max between taking each coin
        """

        if amount == 0:
            return 0

        min_coins = [float("inf")] * (amount + 1)
        min_coins[-1] = 0 # end pos
        for i in range(amount-1, -1, -1):
            for coin in coins:
                if amount - i >= coin:
                    min_coins[i] = min(min_coins[i], min_coins[i+coin]+1)

        if min_coins[0] == float("inf"):
            return -1
        else:
            return min_coins[0]