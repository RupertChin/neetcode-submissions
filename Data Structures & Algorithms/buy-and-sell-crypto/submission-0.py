class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_buy = 101
        # max_sell = -1

        for price in prices:
            if price < min_buy:
                min_buy = price
                # max_sell = -1
            else:
                # max_sell = price
                max_profit = max(max_profit, price - min_buy)
        
        return max_profit
