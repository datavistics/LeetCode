# Given a positive integer num, write a function which returns True if num is a 
# perfect square else False. 
# 
#  Follow up: Do not use any built-in library function such as sqrt. 
# 
#  
#  Example 1: 
#  Input: num = 16
# Output: true
#  Example 2: 
#  Input: num = 14
# Output: false
#  
#  
#  Constraints: 
# 
#  
#  1 <= num <= 2^31 - 1 
#  
#  Related Topics Math Binary Search 
#  👍 1373 👎 196


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # Math
        # sq_int = int(num**.5)
        # return sq_int ** 2 == num

        # Follow up
        l, r = 1, num
        while l <= r:
            mid = l + (r - l) // 2
            mid_s = mid ** 2
            if mid_s == num:
                return True
            elif mid_s < num:
                l = mid + 1
            elif mid_s > num:
                r = mid - 1
        return False


# leetcode submit region end(Prohibit modification and deletion)

s = Solution()
res = s.isPerfectSquare(104976)
print(res)

# Success:
# Runtime:28 ms, faster than 83.48% of Python3 online submissions.
# Memory Usage:14.1 MB, less than 87.40% of Python3 online submissions.
