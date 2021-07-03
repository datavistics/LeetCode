# Given the head of a singly linked list, return true if it is a palindrome. 
# 
#  
#  Example 1: 
# 
#  
# Input: head = [1,2,2,1]
# Output: true
#  
# 
#  Example 2: 
# 
#  
# Input: head = [1,2]
# Output: false
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the list is in the range [1, 105]. 
#  0 <= Node.val <= 9 
#  
# 
#  
# Follow up: Could you do it in O(n) time and O(1) space? Related Topics Linked 
# List Two Pointers Stack Recursion 
#  👍 5718 👎 452
from utilities import ListNode, array2linkedlist


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head.next:
            return True
        slow = head
        fast = head.next
        odd = True
        while slow and fast:
            prev_slow = slow
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next
            else:
                odd = False
        head_left = prev_slow if odd else prev_slow
        head_right = slow.next if odd else slow
        head_left.next = None

        def reverseList(head: ListNode) -> ListNode:
            if not head or not head.next:
                return head

            left, right = head, head.next
            head.next = None
            while left and right:
                temp = right.next
                right.next = left
                left, right = right, temp
            return left

        pl = reverseList(head_right)
        pr = head
        while pl and pr:
            if pl.val == pr.val:
                pl = pl.next
                pr = pr.next
            else:
                return False
        return pl == pr


# leetcode submit region end(Prohibit modification and deletion)

s = Solution()
res = s.isPalindrome(array2linkedlist([1, 1, 2]))
print(res)

# Success:
# Runtime:764 ms, faster than 83.22% of Python3 online submissions.
# Memory Usage:39.5 MB, less than 66.33% of Python3 online submissions.