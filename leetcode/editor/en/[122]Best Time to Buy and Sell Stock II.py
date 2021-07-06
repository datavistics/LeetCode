# You are given an array prices where prices[i] is the price of a given stock on
#  the ith day. 
# 
#  Find the maximum profit you can achieve. You may complete as many transaction
# s as you like (i.e., buy one and sell one share of the stock multiple times). 
# 
#  Note: You may not engage in multiple transactions simultaneously (i.e., you m
# ust sell the stock before you buy again). 
# 
#  
#  Example 1: 
# 
#  
# Input: prices = [7,1,5,3,6,4]
# Output: 7
# Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 
# 5-1 = 4.
# Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
# 
#  
# 
#  Example 2: 
# 
#  
# Input: prices = [1,2,3,4,5]
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 
# 5-1 = 4.
# Note that you cannot buy on day 1, buy on day 2 and sell them later, as you ar
# e engaging multiple transactions at the same time. You must sell before buying a
# gain.
#  
# 
#  Example 3: 
# 
#  
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e., max profit = 0.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= prices.length <= 3 * 104 
#  0 <= prices[i] <= 104 
#  
#  Related Topics Array Dynamic Programming Greedy 
#  👍 4612 👎 2095

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # profit = 0
        # for p1, p2 in zip(prices[:-1], prices[1:]):
        #     if p2 - p1 > 0:
        #         profit += p2 - p1
        # return profit
        state = False
        lo = prev_price = prices[0]
        profit = 0

        for price in prices[1:]:
            prev_state = state
            state = prev_price <= price
            if not state:
                if prev_state:
                    profit += prev_price - lo
                lo = price
            prev_price = price

        # Sell on last day
        if state:
            profit += price - lo

        return profit

# leetcode submit region end(Prohibit modification and deletion)
s = Solution()
res = s.maxProfit([6, 7, 4, 3, 1])
print(res)

# Success:
# Runtime:56 ms, faster than 90.60% of Python3 online submissions.
# Memory Usage:15 MB, less than 87.89% of Python3 online submissions.
