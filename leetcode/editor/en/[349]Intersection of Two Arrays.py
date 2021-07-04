# Given two integer arrays nums1 and nums2, return an array of their intersectio
# n. Each element in the result must be unique and you may return the result in an
# y order. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]
#  
# 
#  Example 2: 
# 
#  
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
# Explanation: [4,9] is also accepted.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums1.length, nums2.length <= 1000 
#  0 <= nums1[i], nums2[i] <= 1000 
#  
#  Related Topics Array Hash Table Two Pointers Binary Search Sorting 
#  👍 1578 👎 1615

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Hash
        return list(set(nums1).intersection(set(nums2)))


# leetcode submit region end(Prohibit modification and deletion)

# Success:
# Runtime:32 ms, faster than 99.70% of Python3 online submissions.
# Memory Usage:14.6 MB, less than 12.01% of Python3 online submissions.