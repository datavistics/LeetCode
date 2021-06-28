# Given an integer array nums where the elements are sorted in ascending order, 
# convert it to a height-balanced binary search tree. 
# 
#  A height-balanced binary tree is a binary tree in which the depth of the two 
# subtrees of every node never differs by more than one. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]
# Explanation: [0,-10,5,null,-3,null,9] is also accepted:
# 
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [1,3]
# Output: [3,1]
# Explanation: [1,3] and [3,1] are both a height-balanced BSTs.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 104 
#  -104 <= nums[i] <= 104 
#  nums is sorted in a strictly increasing order. 
#  
#  Related Topics Array Divide and Conquer Tree Binary Search Tree Binary Tree 
#  👍 4169 👎 291

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'{self.left.__repr__()}{self.val}{self.right.__repr__()}'


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None

        mid = len(nums) // 2
        return TreeNode(nums[mid], left=self.sortedArrayToBST(nums[:mid]), right=self.sortedArrayToBST(nums[mid + 1:]))


# leetcode submit region end(Prohibit modification and deletion)

s = Solution()
nums = [-10, -3, 0, 5, 9]
res = s.sortedArrayToBST(nums)
print(res)

# Success:
# Runtime:52 ms, faster than 96.74% of Python3 online submissions.
# Memory Usage:15.5 MB, less than 86.02% of Python3 online submissions.