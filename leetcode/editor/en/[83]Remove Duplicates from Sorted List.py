# Given the head of a sorted linked list, delete all duplicates such that each e
# lement appears only once. Return the linked list sorted as well. 
# 
#  
#  Example 1: 
# 
#  
# Input: head = [1,1,2]
# Output: [1,2]
#  
# 
#  Example 2: 
# 
#  
# Input: head = [1,1,2,3,3]
# Output: [1,2,3]
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the list is in the range [0, 300]. 
#  -100 <= Node.val <= 100 
#  The list is guaranteed to be sorted in ascending order. 
#  
#  Related Topics Linked List 
#  👍 2786 👎 153

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        cur = search = head
        while search:
            if cur.val != search.val:
                cur.next = search
                cur = cur.next
            search = search.next
        cur.next = None
        return head

# leetcode submit region end(Prohibit modification and deletion)

# Success:
# Runtime:36 ms, faster than 94.09% of Python3 online submissions.
# Memory Usage:14.3 MB, less than 54.94% of Python3 online submissions.