# Reverse bits of a given 32 bits unsigned integer. 
# 
#  Note: 
# 
#  
#  Note that in some languages such as Java, there is no unsigned integer type. 
# In this case, both input and output will be given as a signed integer type. They
#  should not affect your implementation, as the integer's internal binary represe
# ntation is the same, whether it is signed or unsigned. 
#  In Java, the compiler represents the signed integers using 2's complement not
# ation. Therefore, in Example 2 above, the input represents the signed integer -3
#  and the output represents the signed integer -1073741825. 
#  
# 
#  Follow up: 
# 
#  If this function is called many times, how would you optimize it? 
# 
#  
#  Example 1: 
# 
#  
# Input: n = 00000010100101000001111010011100
# Output:    964176192 (00111001011110000010100101000000)
# Explanation: The input binary string 00000010100101000001111010011100 represen
# ts the unsigned integer 43261596, so return 964176192 which its binary represent
# ation is 00111001011110000010100101000000.
#  
# 
#  Example 2: 
# 
#  
# Input: n = 11111111111111111111111111111101
# Output:   3221225471 (10111111111111111111111111111111)
# Explanation: The input binary string 11111111111111111111111111111101 represen
# ts the unsigned integer 4294967293, so return 3221225471 which its binary repres
# entation is 10111111111111111111111111111111.
#  
# 
#  
#  Constraints: 
# 
#  
#  The input must be a binary string of length 32 
#  
#  Related Topics Divide and Conquer Bit Manipulation 
#  👍 1910 👎 607


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for _ in range(32):
            res = (res<<1) + (n&1)
            n>>=1
        return res
        # def flip_bits(n, bits):
        #     left = n >> bits
        #     right = n & (2**bits - 1)
        #     print(bin(left), bin(right))
        #     if bits == 1:
        #         return (right << bits) + left
        #     else:
        #         new_bits = bits//2
        #         return flip_bits(right, new_bits) << new_bits + flip_bits(left, new_bits)
        # return flip_bits(n, 16)
# leetcode submit region end(Prohibit modification and deletion)

s = Solution()
res = s.reverseBits(4294967293)
print(res, bin(res))

# Success:
# Runtime:20 ms, faster than 99.54% of Python3 online submissions.
# Memory Usage:14.4 MB, less than 6.11% of Python3 online submissions.
