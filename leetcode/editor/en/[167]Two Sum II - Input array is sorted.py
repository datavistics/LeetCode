# Given an array of integers numbers that is already sorted in non-decreasing or
# der, find two numbers such that they add up to a specific target number. 
# 
#  Return the indices of the two numbers (1-indexed) as an integer array answer 
# of size 2, where 1 <= answer[0] < answer[1] <= numbers.length. 
# 
#  The tests are generated such that there is exactly one solution. You may not 
# use the same element twice. 
# 
#  
#  Example 1: 
# 
#  
# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
#  
# 
#  Example 2: 
# 
#  
# Input: numbers = [2,3,4], target = 6
# Output: [1,3]
#  
# 
#  Example 3: 
# 
#  
# Input: numbers = [-1,0], target = -1
# Output: [1,2]
#  
# 
#  
#  Constraints: 
# 
#  
#  2 <= numbers.length <= 3 * 104 
#  -1000 <= numbers[i] <= 1000 
#  numbers is sorted in non-decreasing order. 
#  -1000 <= target <= 1000 
#  The tests are generated such that there is exactly one solution. 
#  
#  Related Topics Array Two Pointers Binary Search 
#  👍 2901 👎 753

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1
        while i < j:
            sum = numbers[i] + numbers[j]
            if sum == target:
                return [i + 1, j + 1]
            elif sum < target:
                i += 1
            else:
                j -= 1

        
# leetcode submit region end(Prohibit modification and deletion)
s = Solution()
res = s.twoSum([2,7,11,15], 9)
print(res)

# Success:
# Runtime:52 ms, faster than 99.00% of Python3 online submissions.
# Memory Usage:14.8 MB, less than 30.67% of Python3 online submissions.
# Time:: 00:04:51