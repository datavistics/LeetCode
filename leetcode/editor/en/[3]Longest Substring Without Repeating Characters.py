# Given a string s, find the length of the longest substring without repeating c
# haracters. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
#  
# 
#  Example 2: 
# 
#  
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
#  
# 
#  Example 3: 
# 
#  
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a 
# substring.
#  
# 
#  Example 4: 
# 
#  
# Input: s = ""
# Output: 0
#  
# 
#  
#  Constraints: 
# 
#  
#  0 <= s.length <= 5 * 104 
#  s consists of English letters, digits, symbols and spaces. 
#  
#  Related Topics Hash Table String Sliding Window 
#  👍 15681 👎 778


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        d = {}
        left = 0
        longest = 0
        for right, letter in enumerate(s):
            if letter in d:
                found_dup = d[letter]
                d[letter] = right
                while left <= found_dup:
                    del d[s[left]]
                    left += 1
                    # print(s[left:right])
            d[letter] = right
            # print(s[left:right])
            longest = max(longest, right - left)
        return longest + 1


# leetcode submit region end(Prohibit modification and deletion)

s = Solution.lengthOfLongestSubstring(None, "bbbbbb")
# s = Solution.lengthOfLongestSubstring(None, "abcabcbb")
# s = Solution.lengthOfLongestSubstring(None, "nfpdmpi")
print(s)

# Success:
# Runtime: 68 ms, faster than 56.51% of Python3 online submissions.
# Memory Usage: 14.2 MB, less than 79.09% of Python3 online submissions.
