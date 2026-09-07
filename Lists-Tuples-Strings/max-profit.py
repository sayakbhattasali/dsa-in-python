# Best time to buy and sell (maximum profit)

class Solution:
    def maxProfit(self,prices):
        min_price=prices[0]
        profit=0
        n=len(prices)
        for i in range(1,n):
            current_profit = prices[i]-min_price
            if current_profit>profit:
                profit=current_profit
            min_price=min(min_price,prices[i])
        return profit

num=[int(x) for x in input("enter prices separated by spaces: ").split()]

obj=Solution()
result=obj.maxProfit(num)
print("Max Profit: ",result)
