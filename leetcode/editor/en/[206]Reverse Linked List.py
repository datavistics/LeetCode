# Given the head of a singly linked list, reverse the list, and return the rever
# sed list. 
# 
#  
#  Example 1: 
# 
#  
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
#  
# 
#  Example 2: 
# 
#  
# Input: head = [1,2]
# Output: [2,1]
#  
# 
#  Example 3: 
# 
#  
# Input: head = []
# Output: []
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the list is the range [0, 5000]. 
#  -5000 <= Node.val <= 5000 
#  
# 
#  
#  Follow up: A linked list can be reversed either iteratively or recursively. C
# ould you implement both? 
#  Related Topics Linked List Recursion 
#  👍 7536 👎 142
from utilities import array2linkedlist, ListNode
# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        left, right = head, head.next
        head.next = None
        while left and right:
            temp = right.next
            right.next = left
            left, right = right, temp
        return left

        
# leetcode submit region end(Prohibit modification and deletion)

ll = array2linkedlist([0,1,2])
s = Solution()
s.reverseList(ll)

# Success:
# Runtime:40 ms, faster than 35.19% of Python3 online submissions.
# Memory Usage:15.7 MB, less than 42.28% of Python3 online submissions.
# Time:: 00:17:39