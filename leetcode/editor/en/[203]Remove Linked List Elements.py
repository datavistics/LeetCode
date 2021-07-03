# Given the head of a linked list and an integer val, remove all the nodes of th
# e linked list that has Node.val == val, and return the new head. 
# 
#  
#  Example 1: 
# 
#  
# Input: head = [1,2,6,3,4,5,6], val = 6
# Output: [1,2,3,4,5]
#  
# 
#  Example 2: 
# 
#  
# Input: head = [], val = 1
# Output: []
#  
# 
#  Example 3: 
# 
#  
# Input: head = [7,7,7,7], val = 7
# Output: []
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the list is in the range [0, 104]. 
#  1 <= Node.val <= 50 
#  0 <= val <= 50 
#  
#  Related Topics Linked List Recursion 
#  👍 2929 👎 129
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
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode()
        dummy.next = head
        cur = dummy
        search = head

        while search:
            if search.val != val:
                cur.next = search
                cur = cur.next
            search = search.next
        cur.next = None
        return dummy.next
        
# leetcode submit region end(Prohibit modification and deletion)

# Success:
# Runtime:64 ms, faster than 88.71% of Python3 online submissions.
# Memory Usage:17.1 MB, less than 65.22% of Python3 online submissions.