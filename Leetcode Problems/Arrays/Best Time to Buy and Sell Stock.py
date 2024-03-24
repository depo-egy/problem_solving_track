class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r=0,1
        maxProfit = -000
        while(r<len(prices)):
            if prices[l] < prices[r]:
                difference = prices[r] - prices[l]
                maxProfit = max(maxProfit,difference)
            else:
                l = r
            r +=1
        return maxProfit
