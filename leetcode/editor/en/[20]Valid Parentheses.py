# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']
# ', determine if the input string is valid. 
# 
#  An input string is valid if: 
# 
#  
#  Open brackets must be closed by the same type of brackets. 
#  Open brackets must be closed in the correct order. 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: s = "()"
# Output: true
#  
# 
#  Example 2: 
# 
#  
# Input: s = "()[]{}"
# Output: true
#  
# 
#  Example 3: 
# 
#  
# Input: s = "(]"
# Output: false
#  
# 
#  Example 4: 
# 
#  
# Input: s = "([)]"
# Output: false
#  
# 
#  Example 5: 
# 
#  
# Input: s = "{[]}"
# Output: true
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 104 
#  s consists of parentheses only '()[]{}'. 
#  
#  Related Topics String Stack 
#  👍 7998 👎 327

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s[::-1]:
            # Check for opening or closing
            if c in ')]}':
                stack.append(c)
            else:
                if stack:
                    comp = stack.pop()
                    # Out of order
                    if abs(ord(comp) - ord(c)) > 2:
                        return False
                else:
                    # Unbalanced scenario (more opening)
                    return False

        # Unbalanced scenario (more closing)
        return not bool(stack)

# leetcode submit region end(Prohibit modification and deletion)

# Success:
# Runtime:24 ms, faster than 95.82% of Python3 online submissions.
# Memory Usage:14.5 MB, less than 6.68% of Python3 online submissions.
# Time:: 00:09:20