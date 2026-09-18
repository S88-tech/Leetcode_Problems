# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        if head is None or head.next is None:
            return head
        
        arr = []
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next
            
        k = k % len(arr)
        if k == 0:
            return head
            
        arr = arr[-k:] + arr[:-k]
        
        dummy = ListNode(0)
        curr = dummy
        for value in arr:
            curr.next = ListNode(value)
            curr = curr.next
            
        return dummy.next
        