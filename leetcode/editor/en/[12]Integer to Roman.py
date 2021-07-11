# Roman numerals are represented by seven different symbols: I, V, X, L, C, D an
# d M. 
# 
#  
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000 
# 
#  For example, 2 is written as II in Roman numeral, just two one's added togeth
# er. 12 is written as XII, which is simply X + II. The number 27 is written as XX
# VII, which is XX + V + II. 
# 
#  Roman numerals are usually written largest to smallest from left to right. Ho
# wever, the numeral for four is not IIII. Instead, the number four is written as 
# IV. Because the one is before the five we subtract it making four. The same prin
# ciple applies to the number nine, which is written as IX. There are six instance
# s where subtraction is used: 
# 
#  
#  I can be placed before V (5) and X (10) to make 4 and 9. 
#  X can be placed before L (50) and C (100) to make 40 and 90. 
#  C can be placed before D (500) and M (1000) to make 400 and 900. 
#  
# 
#  Given an integer, convert it to a roman numeral. 
# 
#  
#  Example 1: 
# 
#  
# Input: num = 3
# Output: "III"
#  
# 
#  Example 2: 
# 
#  
# Input: num = 4
# Output: "IV"
#  
# 
#  Example 3: 
# 
#  
# Input: num = 9
# Output: "IX"
#  
# 
#  Example 4: 
# 
#  
# Input: num = 58
# Output: "LVIII"
# Explanation: L = 50, V = 5, III = 3.
#  
# 
#  Example 5: 
# 
#  
# Input: num = 1994
# Output: "MCMXCIV"
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= num <= 3999 
#  
#  Related Topics Hash Table Math String 
#  👍 1952 👎 3316


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def intToRoman(self, num: int) -> str:
        out = ''
        for l in ('IVX', 'XLC', 'CDM'):
            i = num % 10
            if i < 4:
                out = l[0] * i + out
            elif i == 4:
                out = l[0] + l[1] + out
            elif i < 9:
                out = l[1] + l[0] * (i - 5) + out
            else:
                out = l[0] + l[2] + out
            num = num // 10
        out = 'M' * num + out
        return out

# leetcode submit region end(Prohibit modification and deletion)

s = Solution.intToRoman(None, 1994)
print(s)

# Success:
# Runtime: 60 ms, faster than 29.00% of Python3 online submissions.
# Memory Usage: 14.1 MB, less than 82.56% of Python3 online submissions.
