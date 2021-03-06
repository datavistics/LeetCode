# You are given two non-empty linked lists representing two non-negative integer
# s. The digits are stored in reverse order, and each of their nodes contains a si
# ngle digit. Add the two numbers and return the sum as a linked list. 
# 
#  You may assume the two numbers do not contain any leading zero, except the nu
# mber 0 itself. 
# 
#  
#  Example 1: 
# 
#  
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
#  
# 
#  Example 2: 
# 
#  
# Input: l1 = [0], l2 = [0]
# Output: [0]
#  
# 
#  Example 3: 
# 
#  
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in each linked list is in the range [1, 100]. 
#  0 <= Node.val <= 9 
#  It is guaranteed that the list represents a number that does not have leading
#  zeros. 
#  
#  Related Topics Linked List Math Recursion 
#  👍 12713 👎 2909

from utilities import ListNode


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = cur = ListNode()
        carry = 0
        while l1 or l2:
            cur.next = ListNode()
            cur = cur.next
            l1v = l1.val if l1 else 0
            l2v = l2.val if l2 else 0
            carry, cur.val = divmod(l1v + l2v + carry, 10)

            # Nexts
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if carry:
            cur.next = ListNode(carry)
        return dummy.next

# leetcode submit region end(Prohibit modification and deletion)

# Success:
# Runtime: 84 ms, faster than 18.03% of Python3 online submissions.
# Memory Usage: 14.4 MB, less than 43.01% of Python3 online submissions.