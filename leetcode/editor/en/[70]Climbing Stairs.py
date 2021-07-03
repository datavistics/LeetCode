# You are climbing a staircase. It takes n steps to reach the top. 
# 
#  Each time you can either climb 1 or 2 steps. In how many distinct ways can yo
# u climb to the top? 
# 
#  
#  Example 1: 
# 
#  
# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
#  
# 
#  Example 2: 
# 
#  
# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= n <= 45 
#  
#  Related Topics Math Dynamic Programming Memoization 
#  👍 7112 👎 221

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def climbStairs(self, n: int) -> int:
        lookup_arr = [0] * (n + 1)
        def cs(n, lookup_arr):
            if n < 3:
                return n, lookup_arr
            temp = lookup_arr[n]
            if temp:
                return temp, lookup_arr

            val = cs(n - 1, lookup_arr)[0] + cs(n - 2, lookup_arr)[0]
            lookup_arr[n] = val
            return val, lookup_arr
        return cs(n, lookup_arr)[0]

# leetcode submit region end(Prohibit modification and deletion)

s = Solution()
res = s.climbStairs(3)
print(res)

# Success:
# Runtime:24 ms, faster than 94.63% of Python3 online submissions.
# Memory Usage:14.2 MB, less than 42.30% of Python3 online submissions