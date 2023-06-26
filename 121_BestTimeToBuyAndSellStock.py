class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        #To solve this we are using the sliding window principle
        l,r = 0,1
        max_profit = 0
        
        # we start with the left and right pointers next to each other  
        while r < len(prices):
            # if our left pointer is greater than our right then we know we'd be selling at a loss
            # so we set our left to the right, and then increment our right to search for a new number to sell at
            if prices[l] >= prices[r]:
                l = r
                r = r+1
            # if our left is less than our right than we know that we can sell at a profit
            # we have a running total called max profit that has the current highest profit saved to it that we can compare our current profit
            # with and keep the greatest of the two.
            # after that we increment our right pointer to look for an even bigger number make a profit on
            elif prices[l] < prices[r]:
                max_profit = max(max_profit,(prices[r] - prices[l]))
                r = r+1

        return max_profit
