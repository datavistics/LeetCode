# Given two binary strings a and b, return their sum as a binary string. 
# 
#  
#  Example 1: 
#  Input: a = "11", b = "1"
# Output: "100"
#  Example 2: 
#  Input: a = "1010", b = "1011"
# Output: "10101"
#  
#  
#  Constraints: 
# 
#  
#  1 <= a.length, b.length <= 104 
#  a and b consist only of '0' or '1' characters. 
#  Each string does not contain leading zeros except for the zero itself. 
#  
#  Related Topics Math String Bit Manipulation Simulation 
#  👍 2994 👎 365

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return str(bin(int(a, base=2) + int(b, base=2)))[2:]

# leetcode submit region end(Prohibit modification and deletion)

# Success:
# Runtime:32 ms, faster than 76.41% of Python3 online submissions.
# Memory Usage:14.2 MB, less than 52.28% of Python3 online submissions.