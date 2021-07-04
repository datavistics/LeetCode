# Given a string s, determine if it is a palindrome, considering only alphanumer
# ic characters and ignoring cases. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
#  
# 
#  Example 2: 
# 
#  
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 2 * 105 
#  s consists only of printable ASCII characters. 
#  
#  Related Topics Two Pointers String 
#  👍 2173 👎 4017


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        ord_a = ord('a')
        ord_z = ord('z')
        ord_0 = ord('0')
        ord_9 = ord('9')
        ord_A = ord('A')
        ord_Z = ord('Z')
        temp = []
        for c in s:
            c_ord = ord(c)
            if ord_a <= c_ord <= ord_z or ord_0 <= c_ord <= ord_9:
                temp.append(c_ord)
            elif ord_A <= c_ord <= ord_Z:
                c_ord += ord_a - ord_A
                temp.append(c_ord)
        return temp == temp[::-1]
# leetcode submit region end(Prohibit modification and deletion)

s = Solution()
res = s.isPalindrome("A man, a plan, a canal: Panama")
print(res)

# Success:
# Runtime:48 ms, faster than 62.29% of Python3 online submissions.
# Memory Usage:15.4 MB, less than 28.27% of Python3 online submissions.