class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def array2linkedlist(arr):
    dummy = ListNode()
    prev = dummy
    for i in arr:
        temp = ListNode(i)
        prev.next = temp
        prev = temp
    return dummy.next