class Solution:
    def bestTimeToBuyAndSellStock(self, prices: list[int]) -> int:
        min_price = float('inf')
        maxprofit = 0
        profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            profit = price - min_price
            maxprofit = max(maxprofit, profit)
        return maxprofit
prices = [7,1,5,3,6,4]
S1 = Solution()
print(S1.bestTimeToBuyAndSellStock(prices))