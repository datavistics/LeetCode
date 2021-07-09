# There is only one character 'A' on the screen of a notepad. You can perform tw
# o operations on this notepad for each step: 
# 
#  
#  Copy All: You can copy all the characters present on the screen (a partial co
# py is not allowed). 
#  Paste: You can paste the characters which are copied last time. 
#  
# 
#  Given an integer n, return the minimum number of operations to get the charac
# ter 'A' exactly n times on the screen. 
# 
#  
#  Example 1: 
# 
#  
# Input: n = 3
# Output: 3
# Explanation: Intitally, we have one character 'A'.
# In step 1, we use Copy All operation.
# In step 2, we use Paste operation to get 'AA'.
# In step 3, we use Paste operation to get 'AAA'.
#  
# 
#  Example 2: 
# 
#  
# Input: n = 1
# Output: 0
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= n <= 1000 
#  
#  Related Topics Math Dynamic Programming 
#  👍 1949 👎 138


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minSteps(self, n: int) -> int:
        """
        :type n: int
        :rtype: int
        """
        primes = (
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103,
        107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223,
        227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347,
        349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463,
        467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607,
        613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743,
        751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883,
        887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997)
        p_set = set(primes)
        i, total = 0, 0
        while n > 1:
            if n in p_set:
                total += n
                n //= n
            elif n % primes[i] == 0:
                total += primes[i]
                n //= primes[i]
            else:
                i += 1
        return total
        
# leetcode submit region end(Prohibit modification and deletion)

s = Solution.minSteps(None,4)
print(s)

# Success:
# Runtime: 32 ms, faster than 84.25 % of Python3 online submissions.
# Memory Usage: 14.4 MB, less than 20.19 % of Python3 online submissions.